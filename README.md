# Tugas_SNA_kelompok

## Project Description

This project is a web-based calculator application that allows users to perform mathematical calculations through a simple interface.  
The application is containerized using Docker and integrated with GitHub Actions for automated CI/CD and DevSecOps processes.

---

## Technology Stack

- Python
- Flask
- Docker
- GitHub Actions
- Pytest
- Bandit
- pip-audit

---

## Cara Menjalankan Project

Berikut langkah-langkah untuk menjalankan project ini di komputer lokal.

### 1. Install Software yang Dibutuhkan

Pastikan sudah menginstall:

- Git
- Docker Desktop

### 2. Step by Step menjalankan programnya:
1. buka CMD pada device lalu ketik Clone repository ini ke komputer kamu:

   "git clone https://github.com/Nikolas0077/Tugas_SNA_kelompok.git"

   (folder akan ter install pada komputer kamu)
   <img width="1120" height="232" alt="image" src="https://github.com/user-attachments/assets/ffcf125d-73ea-4cd9-b4a5-94dbccd7a49c" />

2. Masuk ke folder project:

   "cd Tugas_SNA_kelompok"

   <img width="528" height="95" alt="image" src="https://github.com/user-attachments/assets/a0be520a-0dc0-4c6e-84d1-4b445192dc5e" />

3. buka Docker Desktop lalu pastikan dalam keadaan running

4. Jalankan perintah berikut untuk membuat Docker Image:

   "docker build -t tugas-sna-app ."
   <img width="2536" height="930" alt="image" src="https://github.com/user-attachments/assets/f39749bd-0403-4c9c-9d65-c85f1a43a75a" />

5. Jalankan container dengan command berikut:

   "docker run -p 8000:8000 tugas-sna-app"
   <img width="1198" height="177" alt="image" src="https://github.com/user-attachments/assets/fe2d2b22-366e-4f95-818a-90cee83b5b3e" />

6. Buka browser lalu akses:

   "http://localhost:8000"
   <img width="1909" height="1016" alt="awal" src="https://github.com/user-attachments/assets/85b853f2-cd9a-41e5-ad18-51c6bc951282" />"

7. program sudah siap untuk digunakan

### 3. cara menggunakan program:
1. ketik hitung" an yang mau anda lakukan
   <img width="445" height="563" alt="2" src="https://github.com/user-attachments/assets/88742025-3763-4060-84ff-c98fb655703a" />"

2. maka output akan berupa hasil dari hitung hitungan yang anda inginkan
   <img width="423" height="531" alt="3" src="https://github.com/user-attachments/assets/d2a1133d-9c69-4841-8591-812ba1415085" />" 

---

## CI/CD Pipeline

This project implements a CI/CD pipeline using GitHub Actions to automate testing and security validation.

### Pipeline Workflow

1. Developer pushes code to GitHub
2. GitHub Actions automatically triggers the workflow
3. Dependencies are installed
4. Automated testing is executed
5. Linting and validation are performed
6. Security scanning is executed
7. Pipeline results are displayed in GitHub Actions

---

## DevSecOps Security Features

### 1. Static Application Security Testing (SAST)
Bandit is used to detect insecure Python code and security vulnerabilities.

### 2. Software Composition Analysis (SCA)
pip-audit is used to identify vulnerable dependencies from third-party packages.

### 3. Secret Scanning
The pipeline checks for potential hardcoded secrets such as passwords or API keys.

---

## Project Structure

```text
.github/workflows   -> CI/CD workflow configuration
src/                -> Application source code
tests/              -> Automated testing files
Dockerfile          -> Docker container configuration
README.md           -> Project documentation
```