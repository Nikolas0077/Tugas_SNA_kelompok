#!/bin/bash
set -e

# Use the platform python
PY=python

# Create venv once under /home (persistent across restarts)
if [ ! -d "/home/venv" ]; then
  $PY -m venv /home/venv
  /home/venv/bin/pip install --upgrade pip wheel
fi

# Install/refresh deps if requirements.txt exists
if [ -f requirements.txt ]; then
  /home/venv/bin/pip install -r requirements.txt
fi

# If gunicorn isn't in requirements, fallback install (optional)
if ! /home/venv/bin/python -c "import gunicorn" 2>/dev/null; then
  /home/venv/bin/pip install gunicorn
fi

export PYTHONPATH=/home/site/wwwroot

# Start app; replace src.app:app if your WSGI path differs
exec /home/venv/bin/gunicorn --workers=2 --threads=4 --timeout=60 \
  --bind 0.0.0.0:${PORT:-8000} src.app:app
