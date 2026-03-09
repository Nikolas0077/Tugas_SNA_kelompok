# Tugas_SNA_kelompok

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
<img width="1191" height="344" alt="image" src="https://github.com/user-attachments/assets/7310ff47-3af7-467a-84d0-4d47781d7c90" />

7. program sudah siap untuk digunakan

### 3. cara menggunakan program:
1. ketik hitung" an yang mau anda lakukan
<img width="807" height="406" alt="image" src="https://github.com/user-attachments/assets/00cdd36f-4e13-45e1-959f-08799d6fba36" />

2. maka output akan berupa hasil dari hitung hitungan yang anda inginkan
   <img width="788" height="283" alt="image" src="https://github.com/user-attachments/assets/517f1102-33ca-4ee8-8f6a-c3e5c215d39b" />

