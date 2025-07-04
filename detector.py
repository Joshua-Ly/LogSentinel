from collections import defaultdict
from datetime import timedelta

failed_login_attempts = defaultdict(list)

def detect_bruteforce(log_entry):
    if log_entry['level'] == 'WARNING' and 'Failed login' in log_entry['message']:
        ip = log_entry['message'].split("from IP ")[-1]
        failed_login_attempts[ip].append(log_entry['timestamp'])

        failed_login_attempts[ip] = [
            t for t in failed_login_attempts[ip]
            if log_entry['timestamp'] - t < timedelta(minutes=1)
        ]

        if len(failed_login_attempts[ip]) >= 3:
            return f"[ALERT] Possible brute-force attack from IP {ip}"
    return None
