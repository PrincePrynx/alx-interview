#!/usr/bin/python3
import sys
import signal

# Dictionary to keep the count of status codes
status_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

total_size = 0
line_count = 0

def print_statistics():
    print("File size: {}".format(total_size))
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print("{}: {}".format(status, status_counts[status]))

def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

# Register the signal handler for keyboard interrupt
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 9:
            continue
        ip, _, _, date, method, url, protocol, status_code, file_size = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7], parts[8]
        
        # Validate and process the extracted parts
        if method != "\"GET" or url != "/projects/260" or protocol != "HTTP/1.1\"":
            continue
        try:
            status_code = status_code.strip()
            file_size = int(file_size.strip())
            if status_code in status_counts:
                status_counts[status_code] += 1
                total_size += file_size
                line_count += 1
        except ValueError:
            continue
        
        if line_count % 10 == 0:
            print_statistics()
except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)
