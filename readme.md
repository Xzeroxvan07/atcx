# Advanced Auto Clicker

Auto clicker canggih dengan berbagai fitur untuk game dan aplikasi yang membutuhkan klik berulang dengan kecepatan tinggi.

## Fitur

- ⚡ Kecepatan klik yang dapat disesuaikan (hingga 1000 klik per detik)
- 📍 Pengaturan posisi klik tetap
- 🖱️ Dukungan klik kiri, kanan, dan tengah
- 🔄 Klik tunggal, ganda, atau tripel
- 💾 Sistem profil untuk menyimpan dan memuat pengaturan
- 📊 Statistik klik real-time
- ⌨️ Hotkey untuk semua fungsi

## Persyaratan

- Python 3.6 atau lebih tinggi
- Libraries: pyautogui, keyboard, pynput

## Instalasi

```bash
# Clone repositori
git clone https://github.com/username/advanced-auto-clicker.git
cd advanced-auto-clicker

# Instal dependencies
pip install pyautogui keyboard pynput
```

## Penggunaan

```bash
# Jalankan dengan pengaturan default
python autoclicker.py

# Jalankan dengan kecepatan kustom
python autoclicker.py --speed 0.001

# Jalankan dengan profil tersimpan
python autoclicker.py --profile game1
```

## Kontrol Keyboard

| Tombol | Fungsi |
|--------|--------|
| F6 | Mulai/Hentikan auto clicking |
| F7 | Tingkatkan kecepatan klik |
| F8 | Kurangi kecepatan klik |
| F9 | Keluar dari program |
| F10 | Ganti jenis klik (tunggal/ganda/tripel) |
| F11 | Ganti tombol klik (kiri/kanan/tengah) |
| F2 | Simpan cepat profil saat ini |
| F3 | Tampilkan daftar profil tersimpan |
| Klik Tengah | Tetapkan posisi klik |

## Sistem Profil

Auto Clicker menyimpan konfigurasi dalam file JSON di folder `profiles/`. Setiap profil menyimpan:

- Kecepatan klik
- Jenis klik (tunggal/ganda/tripel)
- Tombol klik (kiri/kanan/tengah)
- Posisi klik (opsional)

## Kontribusi

Kontribusi sangat diterima! Silakan buka Issues atau Pull Requests.

## Lisensi

[MIT](LICENSE)
