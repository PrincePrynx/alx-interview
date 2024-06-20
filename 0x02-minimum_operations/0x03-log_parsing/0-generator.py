import random
import time

# Possible status codes and their distribution probabilities
status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
status_code_probabilities = [0.5, 0.1, 0.05, 0.05, 0.05, 0.1, 0.1, 0.05]

def generate_log_line():
    """Generates a single log line in the specified format."""
    ip_address = f"192.168.{random.randint(0, 255)}.{random.randint(0, 255)}"
    date = time.strftime("%d/%b/%Y:%H:%M:%S %z", time.localtime())
    request = 'GET /projects/260 HTTP/1.1'
    status_code = random.choices(status_codes, status_code_probabilities)[0]
    file_size = random.randint(500, 5000)
    
    log_line = f"{ip_address} - [{date}] \"{request}\" {status_code} {file_size}"
    return log_line

def main():
    try:
        while True:
            print(generate_log_line())
            time.sleep(1)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
