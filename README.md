Log sentinel is a python-based tool designed to simulate blue team automation. More specifically, it parses custom log formats, detects brute-force login attempts, and resultingly, raises an alert.

# Features
- Parses custom-formatted logs
- Detects brute-force login attempts(3+ failed logins in a minute or less)
- Raises console alerts upon detection
- Easy to extend with other detection-based logic

# Planned Features
- Real-time log monitoring
- Slack/email alerts
- Configurable detection rules (YAML)
- Web UI (Flask) for displaying alerts
- Docker support for easy deployment

# Requirements To Run Logsentinel
- Python 3.7+

# To Run Logsentinel
```bash
python main.py

