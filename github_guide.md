# Cara Menyimpan Project Auto Clicker di GitHub

Berikut adalah panduan langkah demi langkah untuk menyimpan project Auto Clicker Anda ke GitHub:

## 1. Persiapan Awal

### Instal Git
Jika belum memiliki Git:
- Download dan instal Git dari [git-scm.com](https://git-scm.com/downloads)
- Setelah instalasi, buka terminal atau command prompt untuk memverifikasi instalasi:
  ```
  git --version
  ```

### Buat Akun GitHub
Jika belum memiliki akun GitHub:
- Kunjungi [github.com](https://github.com/) dan daftar akun baru
- Verifikasi email Anda

## 2. Siapkan Repository Lokal

### Siapkan Folder Project
1. Buat folder baru untuk project Anda:
   ```
   mkdir advanced-auto-clicker
   cd advanced-auto-clicker
   ```

2. Simpan file `autoclicker.py` ke dalam folder ini

3. Buat folder profiles di dalam folder project:
   ```
   mkdir profiles
   ```

4. Tambahkan file `README.md` dengan konten yang telah diberikan

### Inisialisasi Git Repository
1. Buka terminal/command prompt dan navigasi ke folder project Anda
2. Inisialisasi repository Git baru:
   ```
   git init
   ```

3. Tambahkan semua file ke staging area:
   ```
   git add .
   ```

4. Buat commit pertama:
   ```
   git commit -m "Initial commit: Advanced Auto Clicker"
   ```

## 3. Buat Repository di GitHub

1. Login ke akun GitHub Anda
2. Klik tombol "+" di pojok kanan atas dan pilih "New repository"
3. Isi informasi repository:
   - Repository name: `advanced-auto-clicker`
   - Description: "Auto clicker canggih dengan berbagai fitur untuk game"
   - Visibility: Public atau Private sesuai preferensi Anda
   - Jangan centang opsi "Initialize this repository with a README"
4. Klik "Create repository"

## 4. Hubungkan & Push ke GitHub

### Hubungkan Repository Lokal dengan GitHub
1. Setelah membuat repository, GitHub akan menampilkan instruksi
2. Salin perintah yang terlihat seperti ini:
   ```
   git remote add origin https://github.com/username/advanced-auto-clicker.git
   ```
3. Jalankan perintah tersebut di terminal Anda

### Push Code ke GitHub
1. Push kode Anda ke GitHub:
   ```
   git push -u origin master
   ```
   atau
   ```
   git push -u origin main
   ```
   (tergantung nama branch default Anda)

2. Masukkan username dan password GitHub jika diminta
   - Catatan: GitHub sekarang menggunakan token personal access (PAT) daripada password
   - Jika diminta, buat PAT di Settings > Developer settings > Personal access tokens

## 5. Verifikasi Upload

1. Refresh halaman GitHub repository Anda
2. Semua file seharusnya sudah tampil di repository GitHub
3. README.md akan ditampilkan secara otomatis di halaman depan repository

## 6. Memperbarui Project di Kemudian Hari

Setiap kali Anda membuat perubahan dan ingin mengupdate repository:

1. Simpan perubahan Anda
2. Tambahkan file yang diubah ke staging area:
   ```
   git add .
   ```
3. Buat commit baru:
   ```
   git commit -m "Deskripsi perubahan yang Anda buat"
   ```
4. Push ke GitHub:
   ```
   git push
   ```

## Troubleshooting Umum

- **Error authentication**: Pastikan menggunakan personal access token jika menggunakan HTTPS
- **Conflict saat merge**: Pull dulu perubahan terbaru, selesaikan conflict, lalu push ulang
- **File besar tidak bisa di-push**: GitHub memiliki batasan ukuran file, hindari file data besar

## Fitur GitHub Lainnya yang Berguna

- **Issues**: Untuk melacak bug dan fitur yang diinginkan
- **Pull Requests**: Untuk kolaborasi dengan orang lain
- **GitHub Pages**: Untuk membuat halaman web dokumentasi project Anda
- **Actions**: Untuk continuous integration dan delivery
