import re
from datetime import datetime

log_pattern = r'\[(.*?)\] \[(.*?)\] \[(.*?)\] (.*)'

def parse_log_line(line):
    match = re.match(log_pattern, line)
    if match:
        timestamp, category, level, message = match.groups()
        return {
            'timestamp': datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S'),
            'category': category,
            'level': level,
            'message': message
        }
    return None
