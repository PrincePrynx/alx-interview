#!/usr/bin/python3

import sys
import signal

# Initialize metrics
total_size = 0
status_code_counts = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

def print_metrics():
    """Prints the total file size and status code counts."""
    print(f"File size: {total_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

def signal_handler(sig, frame):
    """Handles keyboard interruption (CTRL + C) to print metrics."""
    print_metrics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

line_count = 0

for line in sys.stdin:
    try:
        parts = line.split()
        if len(parts) != 7:
            continue
        
        ip_address = parts[0]
        date = parts[3] + ' ' + parts[4]
        request = parts[5] + ' ' + parts[6] + ' ' + parts[7]
        status_code = parts[8]
        file_size = parts[9]

        if not status_code.isdigit() or not file_size.isdigit():
            continue

        file_size = int(file_size)
        total_size += file_size

        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
        
        line_count += 1
        if line_count % 10 == 0:
            print_metrics()
    except Exception:
        continue

# Print metrics one last time if end of input is reached
print_metrics()
