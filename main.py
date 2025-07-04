from log_parser import parse_log_line
from detector import detect_bruteforce
from alerts import send_alert

def monitor_log_file(filepath):
    with open(filepath, 'r') as f:
        for line in f:
            parsed = parse_log_line(line.strip())
            if parsed:
                alert = detect_bruteforce(parsed)
                if alert:
                    send_alert(alert)

if __name__ == "__main__":
    monitor_log_file('auth.log')
