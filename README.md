<img width="1120" height="232" alt="image" src="https://github.com/user-attachments/assets/12f37442-baa2-4908-b010-c15fb6e31df5" /># Tugas_SNA_kelompok

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
   <img width="1120" height="232" alt="image" src="https://github.com/user-attachments/assets/ffcf125d-73ea-4cd9-b4a5-94dbccd7a49c" />

3. Masuk ke folder project:
   cd Tugas_SNA_kelompok
   
4. buka Docker Desktop lalu pastikan dalam keadaan running

5. Jalankan perintah berikut untuk membuat Docker Image:
    docker build -t tugas-sna-app .

6. Jalankan container dengan command berikut:
    docker run -p 8000:8000 tugas-sna-app

7. Buka browser lalu akses:
    http://localhost:8000

8. program sudah siap untuk digunakan
