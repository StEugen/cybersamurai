#!/usr/bin/env python3
"""
check_node_vulns - CLI to scan package.json and package-lock.json for vulnerable packages
based on a vulns.txt file.

Usage:
  ./check_node_vulns --package-json package.json --lock-file package-lock.json --vulns vulns.txt
"""

import argparse
import json
import os
import re
import sys

# ---------- Version comparison helpers ----------

def normalize_ver(v: str):
    """
    Normalize version string:
    - strip leading 'v' or whitespace
    - split main and prerelease (on '-')
    Returns (main_parts: list[str], prerelease: str|None)
    """
    if v is None:
        return ([], None)
    s = str(v).strip()
    if s.startswith("v") or s.startswith("V"):
        s = s[1:]
    if s == "":
        return ([], None)
    parts = s.split("-", 1)
    main = parts[0]
    prerelease = parts[1] if len(parts) > 1 else None
    main_parts = main.split(".")
    return (main_parts, prerelease)

def part_to_int(p: str):
    try:
        return int(p)
    except Exception:
        # fallback: non-numeric components compare lexicographically
        return p

def compare_versions(a: str, b: str) -> int:
    """
    Compare semantic-like versions a and b.
    Returns -1 if a < b, 0 if equal, 1 if a > b.
    This is a tolerant comparator (handles numeric and non-numeric parts, prerelease).
    """
    a_main, a_pre = normalize_ver(a)
    b_main, b_pre = normalize_ver(b)

    maxlen = max(len(a_main), len(b_main))
    for i in range(maxlen):
        ai = a_main[i] if i < len(a_main) else "0"
        bi = b_main[i] if i < len(b_main) else "0"
        ai_val = part_to_int(ai)
        bi_val = part_to_int(bi)

        if isinstance(ai_val, int) and isinstance(bi_val, int):
            if ai_val < bi_val:
                return -1
            if ai_val > bi_val:
                return 1
        else:

            ai_s = str(ai_val)
            bi_s = str(bi_val)
            if ai_s < bi_s:
                return -1
            if ai_s > bi_s:
                return 1

    if a_pre is None and b_pre is None:
        return 0
    if a_pre is None and b_pre is not None:
        return 1
    if a_pre is not None and b_pre is None:
        return -1

    a_pr_parts = a_pre.split(".")
    b_pr_parts = b_pre.split(".")
    maxpr = max(len(a_pr_parts), len(b_pr_parts))
    for i in range(maxpr):
        ai = a_pr_parts[i] if i < len(a_pr_parts) else ""
        bi = b_pr_parts[i] if i < len(b_pr_parts) else ""
        ai_val = part_to_int(ai) if ai != "" else ""
        bi_val = part_to_int(bi) if bi != "" else ""
        if isinstance(ai_val, int) and isinstance(bi_val, int):
            if ai_val < bi_val:
                return -1
            if ai_val > bi_val:
                return 1
        else:
            ai_s = str(ai_val)
            bi_s = str(bi_val)
            if ai_s < bi_s:
                return -1
            if ai_s > bi_s:
                return 1
    return 0

def eval_constraint(installed: str, operator: str, vuln_ver: str) -> bool:
    """
    Return True if installed version satisfies the vulnerable constraint.
    operator: one of '==', ':=', '=', '<=', '>=', '<', '>'
    """
    cmp = compare_versions(installed, vuln_ver)
    if operator in ("==", "=", ":="):
        return cmp == 0
    if operator == "<=":
        return cmp <= 0
    if operator == ">=":
        return cmp >= 0
    if operator == "<":
        return cmp < 0
    if operator == ">":
        return cmp > 0

    return False

# ---------- File parsing ----------

VULN_LINE_RE = re.compile(r'^\s*([\w@/.\-]+)\s*(==|:=|=|<=|>=|<|>)\s*([^\s]+)\s*$')

def parse_vulns_file(path: str):
    """
    Parse vulns.txt lines into dict: {pkg_name: [(op, version), ...], ...}
    """
    vulns = {}
    with open(path, encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            m = VULN_LINE_RE.match(line)
            if not m:
                print(f"Warning: couldn't parse vuln line: {line}", file=sys.stderr)
                continue
            name, op, ver = m.group(1), m.group(2), m.group(3)
            vulns.setdefault(name, []).append((op, ver))
    return vulns

def gather_from_package_json(path: str):
    """
    Return dict {pkg_name: version_spec} from package.json (dependencies and friends).
    For package.json, versions are often ranges (like ^1.2.3). We'll attempt to extract a concrete
    version if possible by stripping range prefixes. We keep the raw spec as fallback.
    """
    if not os.path.isfile(path):
        return {}
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    found = {}
    for key in ("dependencies", "devDependencies", "peerDependencies", "optionalDependencies"):
        deps = data.get(key) or {}
        for name, spec in deps.items():

            if isinstance(spec, str):
                spec_str = spec.strip()

                cleaned = re.sub(r'^[\^~><=]*\s*', '', spec_str)

                cleaned = cleaned.split(" ")[0]
                found[name] = cleaned
            else:
                found[name] = str(spec)
    return found

def gather_from_package_lock(path: str):
    """
    Parse package-lock.json and extract resolved installed versions.
    Support both "dependencies" structure and top-level "packages" structure.
    Returns dict {pkg_name: version}
    """
    if not os.path.isfile(path):
        return {}
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    results = {}

    packages_obj = data.get("packages")
    if isinstance(packages_obj, dict):
        for pkg_path, info in packages_obj.items():
            if pkg_path == "" or not pkg_path.startswith("node_modules"):
                continue
            rel = pkg_path[len("node_modules/"):] if pkg_path.startswith("node_modules/") else pkg_path
            name = rel
            ver = info.get("version")
            if ver:
                results[name] = ver

    def walk_deps(dep_map):
        for name, info in (dep_map.items() if isinstance(dep_map, dict) else []):
            if name in results:
                pass
            ver = None
            if isinstance(info, dict):
                ver = info.get("version") or info.get("resolved") or None
            if ver:
                results[name] = ver
            # nested deps
            nested = info.get("dependencies") if isinstance(info, dict) else None
            if isinstance(nested, dict):
                walk_deps(nested)

    deps = data.get("dependencies")
    if isinstance(deps, dict):
        walk_deps(deps)

    return results

# ---------- Checking logic ----------

def find_vulns(installed_map: dict, vulns_map: dict):
    """
    installed_map: {pkg_name: version}
    vulns_map: {pkg_name: [(op, version), ...]}
    returns list of dicts with vulnerability info
    """
    findings = []
    for pkg, vuln_patterns in vulns_map.items():
        if pkg not in installed_map:
            continue
        inst_ver = installed_map[pkg]
        for op, vver in vuln_patterns:
            try:
                if eval_constraint(inst_ver, op, vver):
                    findings.append({
                        "package": pkg,
                        "installed": inst_ver,
                        "vulnerable_constraint": f"{op}{vver}"
                    })
            except Exception as e:
                print(f"Error comparing {pkg} {inst_ver} {op}{vver}: {e}", file=sys.stderr)
    return findings

# ---------- CLI ----------

def main(argv=None):
    parser = argparse.ArgumentParser(prog="check_node_vulns", description="Scan package.json and package-lock.json for vulnerable packages listed in vulns.txt")
    parser.add_argument("--package-json", "-p", default="package.json", help="path to package.json")
    parser.add_argument("--lock-file", "-l", default="package-lock.json", help="path to package-lock.json")
    parser.add_argument("--vulns", "-v", default="vulns.txt", help="path to vulns.txt")
    parser.add_argument("--json", action="store_true", help="output machine-readable JSON")
    parser.add_argument("--quiet", action="store_true", help="suppress warnings")
    args = parser.parse_args(argv)

    if not os.path.isfile(args.vulns):
        print(f"vulns file not found: {args.vulns}", file=sys.stderr)
        return 2

    vulns_map = parse_vulns_file(args.vulns)
    pkgjson_map = gather_from_package_json(args.package_json)
    lock_map = gather_from_package_lock(args.lock_file)

    combined = {}
    combined.update(pkgjson_map)
    combined.update(lock_map)

    if not args.quiet:
        print(f"Packages found in package.json: {len(pkgjson_map)}")
        print(f"Packages found in lock-file: {len(lock_map)}")
        print(f"Total packages considered: {len(combined)}")

    findings = find_vulns(combined, vulns_map)

    if args.json:
        out = {"findings": findings, "counts": {"found": len(findings)}}
        print(json.dumps(out, indent=2))
    else:
        if not findings:
            print("\nNo vulnerable packages found (based on provided vulns.txt).")
        else:
            print("\nVULNERABILITIES FOUND:")
            for f in findings:
                print(f" - {f['package']}: installed {f['installed']} matches {f['vulnerable_constraint']}")
            print(f"\n{len(findings)} vulnerable package(s) detected.")

    return 1 if findings else 0

if __name__ == "__main__":
    try:
        rc = main()
        sys.exit(rc)
    except KeyboardInterrupt:
        print("Interrupted", file=sys.stderr)
        sys.exit(2)
