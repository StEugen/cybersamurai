#!/usr/bin/python3

import argparse
import json
from datetime import datetime

def search_log_for_time(log_file, target_time, time_range=None):

    found_entries = []
    found = False
    error_count = 0
    max_errors_to_show = 5

    try:
        with open(log_file, 'r') as file:
            for line in file:
                line = line.strip()
                    if error_count < max_errors_to_show:
                        print(f"Skipping non-JSON line: {line}")
                    error_count += 1
                    continue

                try:
                    log_entry = json.loads(line)
                    entry_time_str = log_entry.get('timestamp')

                    if entry_time_str is None:
                        if error_count < max_errors_to_show:
                            print(f"Skipping line due to missing timestamp: {line}")
                        error_count += 1
                        continue

                    # Convert "Z" (UTC) to "+00:00" for compatibility with fromisoformat()
                    entry_time = datetime.fromisoformat(entry_time_str.replace("Z", "+00:00"))

                    if time_range:
                        start_time, end_time = time_range
                        if start_time <= entry_time <= end_time:
                            found_entries.append(line)
                    elif found or entry_time == target_time:
                        found_entries.append(line)
                        found = True
                except json.JSONDecodeError:
                    if error_count < max_errors_to_show:
                        print(f"Skipping invalid JSON line: {line}")
                    error_count += 1
                    continue
                except ValueError as e:
                    if error_count < max_errors_to_show:
                        print(f"Skipping line due to timestamp parsing error: {line} ({e})")
                    error_count += 1
                    continue

        if error_count >= max_errors_to_show:
            print(f"Skipped {error_count} non-JSON lines in total.")

    except KeyboardInterrupt:
        print("\nProcess interrupted. Exiting...")
        exit(1)

    return found_entries

def parse_time_range(time_range):

    try:
        start_time_str, end_time_str = time_range.split(',')
        start_time = datetime.fromisoformat(start_time_str.strip())
        end_time = datetime.fromisoformat(end_time_str.strip())
        return start_time, end_time
    except ValueError as e:
        print(f"Error parsing time range: {time_range} ({e})")
        exit(1)

def main():

    parser = argparse.ArgumentParser(description='Cuts log file by time or within a time range.')
    parser.add_argument('log_file', type=str, help='Path to the log file')
    parser.add_argument('target_time', type=str, nargs='?',
                        help='Target time (cuts from that time to the end) (format: YYYY-MM-DDTHH:MM:SS+HH:MM)')
    parser.add_argument('-r', '--range', dest='time_range',
                        type=parse_time_range, metavar='start_time,end_time',
                        help='Search within the specified range (format: "YYYY-MM-DDTHH:MM:SS+HH:MM,YYYY-MM-DDTHH:MM:SS+HH:MM")')
    args = parser.parse_args()

    if args.target_time is None and args.time_range is None:
        print("Error: Please provide either a target time or a time range.")
        exit(1)

    found_entries = search_log_for_time(args.log_file, args.target_time, args.time_range)

    if found_entries:
        output_filename = f"{args.log_file.rsplit('.', 1)[0]}_cut.log"
        with open(output_filename, 'w') as output_file:
            output_file.writelines(found_entries)

        if args.time_range:
            print(f"Extracted {len(found_entries)} log entries within the time range: {args.time_range}")
        else:
            print(f"Extracted {len(found_entries)} log entries from time: {args.target_time}")
        print(f"Saved to: {output_filename}")
    else:
        print("No matching log entries found.")

if __name__ == "__main__":
    main()
