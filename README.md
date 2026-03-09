# Tugas_SNA_kelompok# DevOps Calculator

Web calculator built using Flask and deployed using DevOps

## Features

- Basic calculator operations
- Square root calculation
- Natural logarithm calculation

## Local Run

Install dependencies

pip install -r requirements.txt

Run the application

python src/app.py

## Docker Run

Build Docker image

docker build -t calculator-app .

Run container

docker run -p 8000:8000 calculator-app

Open browser

http://localhost:8000