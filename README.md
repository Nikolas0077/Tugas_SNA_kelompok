# Tugas_SNA_kelompok

## Cara Menjalankan Project

Berikut langkah-langkah untuk menjalankan project ini di komputer lokal.

### 1. Install Software yang Dibutuhkan

Pastikan sudah menginstall:

- Git
- Docker Desktop

### 2. Step by Step menjalankan programnya:
1. buka CMD pada device lalu ketik Clone repository ini ke komputer kamu:
git clone https://github.com/Nikolas0077/Tugas_SNA_kelompok.git
(folder akan ter install pada komputer kamu)
   
2. Masuk ke folder project:
   cd Tugas_SNA_kelompok
   
3. buka Docker Desktop lalu pastikan dalam keadaan running

4. Jalankan perintah berikut untuk membuat Docker Image:
    docker build -t tugas-sna-app .

5. Jalankan container dengan command berikut:
    docker run -p 8000:8000 tugas-sna-app

6. Buka browser lalu akses:
    http://localhost:8000

7. program sudah siap untuk digunakan
