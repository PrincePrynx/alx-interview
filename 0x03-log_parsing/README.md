# LOG PARSING

 Applying knowledge of Python programming, focusing on parsing and processing data streams in real-time. This project involves reading from standard input (stdin), handling data in a specific format, and performing calculations based on the input data

# Log Parser

This project is a Python script that reads log lines from standard input and computes statistics. It prints the total file size and the number of lines for each status code every 10 lines or when interrupted by a keyboard interrupt (Ctrl + C).

## Requirements

- Python 3.4.3 or later
- The script should be executable
- The script should follow PEP 8 style guidelines

## Usage

To use this script, you can pipe log lines into it:

```sh
cat log_file | ./log_parser.py
