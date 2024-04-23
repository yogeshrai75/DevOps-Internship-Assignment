
# Log Monitor and Analyzer
This Python script automates the monitoring and basic analysis of log files.

# Features:
Continuously monitors a specified log file for new entries using tail.
Analyzes entries for occurrences of predefined keywords or patterns.
Generates a summary report with counts for each keyword found.
Handles Ctrl+C for graceful termination and report generation.

# Requirements:
Python 3

# How to Use:
Update Configuration:
Replace "/path/to/your/logfile.log" in the script with the actual path to your log file.
Modify the keywords list in the script to include the specific keywords or error codes you want to track (e.g., "error", "warning", "404").
Also define dictionary to store error counts, and a variable for the summary report.
Save the Script.
Run the Script:
Open a terminal and navigate to the directory where you saved the script.

# Run the script using the following command:
Bash
python log_monitor.py
The script will start monitoring the log file and print new entries along with a summary report upon termination (Ctrl+C).

# Error Handling:
The script handles Ctrl+C interrupt (Ctrl+C) to gracefully terminate the monitoring, generate a report, and exit.
