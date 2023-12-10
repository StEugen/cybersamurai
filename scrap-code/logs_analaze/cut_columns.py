#This script cuts only certain type of files and columns made by atop
# example
# PID SYSCPU USRCPU  VGROW  RGROW  RDDSK  WRDSK  THR S CPUNR  CPU CMD
#10000  1.62s 1.93s     0K     0K   500K  1700K   67 S     0   5% python
#10000  1.55s 1.71s     0K     0K   500K  1700K   33 S     2   5% python
#10000  1.45s 1.31s     0K     0M   500K  1700K   13 S     1   4% python
#10000  1.92s 1.13s     0K     0K   500K  1700K  160 S     3   3% python
#10000  1.00s 1.84s     0K     0K   500K  1700K   32 S     2   2% python


import re

# Function to parse the line and extract PID, WRDSK, and CMD
def parse_line(line):
    match = re.match(r'\s*(\d+)\s+(\S+)\s+\S+\s+\S+\s+\S+\s+(\S+)\s+\S+\s+\S+\s+\S+\s+\S+\s+(.*)', line)
    if match:
        pid = int(match.group(1))
        wrdsk = match.group(2)
        cmd = match.group(4)
        return pid, wrdsk, cmd
    return None

# Function to process the file and filter lines
def process_file(file_path, output_file_path):
    with open(file_path, 'r') as file, open(output_file_path, 'w') as output_file:
        for line in file:
            data = parse_line(line)
            if data:
                wrdsk_numeric_match = re.search(r'([+-]?\d+(\.\d+)?)', data[1])
                if wrdsk_numeric_match:
                    wrdsk_numeric = float(wrdsk_numeric_match.group(1))
                    if wrdsk_numeric > 100:
                        output_file.write(f'PID: {data[0]}, WRDSK: {data[1]}, CMD: {data[2]}\n')

# Accept file path and output file name from user input
file_path = input("Enter the path to the text file: ")
output_file_name = input("Enter the name of the output file: ")
output_file_path = output_file_name.strip()

process_file(file_path, output_file_path)

print(f'Output saved to {output_file_path}')




