@echo off
REM --- activate venv (adjust path if your venv is elsewhere) ---
call .venv\Scripts\activate

REM --- run Flask by pointing to the module inside src ---
python -m flask --app src.app:app run --debug --port 8000
