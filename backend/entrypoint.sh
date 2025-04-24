#!/bin/sh
uvicorn src.app:app --host 0.0.0.0 --port 8000 &
# python src/tasks/wazuh_alert_listener.py
python -m src.tasks.wazuh_alert_listener