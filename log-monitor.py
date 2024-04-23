import signal
import re

# Define variables
log_file = "/path/to/your/logfile.log"  # Replace with your log file path
keywords = ["error", "warning", "404"]  # List of keywords to track
error_counts = {}
summary_report = ""

def signal_handler(sig, frame):
    print("\nTerminating monitoring...")
    generate_report()
    exit(0)

def analyze_log_entry(line):
    for keyword in keywords:
        if re.search(keyword, line):
            if keyword not in error_counts:
                error_counts[keyword] = 0
            error_counts[keyword] += 1

def generate_report():
    global summary_report
    summary_report = f"\nLog Analysis Summary:\n"
    for keyword, count in error_counts.items():
        summary_report += f"{keyword}: {count} occurrences\n"
    print(summary_report)

def monitor_log():
    with open(log_file, "r") as log:
        # Seek to the end of the file initially
        log.seek(0, 2)

        # Handle KeyboardInterrupt (Ctrl+C)
        signal.signal(signal.SIGINT, signal_handler)

        while True:
            line = log.readline()
            if not line:
                continue  # No new entries, wait for more
            analyze_log_entry(line.strip())
            print(line, end="")  # Print new log entry

if __name__ == "__main__":
    print("Starting log monitoring...")
    monitor_log()
