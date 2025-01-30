#!/usr/bin/python3

import argparse
import json
from datetime import datetime, timedelta

def search_log_for_time(log_file, target_time, time_range=None):
    found_entries = []
    found = False
    with open(log_file, 'r') as file:
        for line in file:
            try:
                log_entry = json.loads(line)
                entry_time_str = log_entry.get('time')
                entry_time = datetime.fromisoformat(entry_time_str)
                if time_range:
                    start_time, end_time = time_range
                    if start_time <= entry_time <= end_time:
                        found_entries.append(line)
                elif found or entry_time == target_time:
                    found_entries.append(line)
                    found = True
            except json.JSONDecodeError:
                pass
    
    return found_entries

def parse_time_range(time_range):
    start_time_str, end_time_str = time_range.split(',')
    start_time = datetime.fromisoformat(start_time_str.strip())
    end_time = datetime.fromisoformat(end_time_str.strip())
    return start_time, end_time

def main():
    parser = argparse.ArgumentParser(description='Cuts log file by time or within a time range.')
    parser.add_argument('log_file', type=str, help='log file')
    parser.add_argument('target_time', type=str, nargs='?', 
                        help='Target time (will cut from that time to the end) (format: YYYY-MM-DDTHH:MM:SS+HH:MM)')
    parser.add_argument('-r', '--range', dest='time_range', 
                        type=parse_time_range, metavar='start_time,end_time', 
                        help='Search within the specified range (format: "YYYY-MM-DDTHH:MM:SS+HH:MM,YYYY-MM-DDTHH:MM:SS+HH:MM")')
    args = parser.parse_args()

    if args.target_time is None and args.time_range is None:
        print("Please provide either a target time or a time range.")
        return

    found_entries = search_log_for_time(args.log_file, args.target_time, args.time_range)

    if found_entries:
        if args.time_range:
            print("Found entries within the time range:", args.time_range)
        else:
            print("Found entries at time:", args.target_time)
        with open(f'{args.log_file[:args.log_file.index(".")]}_cut.log', 'w') as output_file:
            for entry in found_entries:
                output_file.write(entry)
    else:
        if args.time_range:
            print("No entries found within the time range:", args.time_range)
        else:
            print("No entries found at time:", args.target_time)

if __name__ == "__main__":
    main()

