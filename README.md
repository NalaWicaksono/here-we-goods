link deploy PWS: https://nalakrishna-abimanyu-here-we-goods.pbp.cs.ui.ac.id/
1.
- Buat proyek dan app main, daftarkan di INSTALLED_APPS. 
- Definisikan Product dengan 6 atribut wajib di models.py.
- Jalankan makemigrations lalu migrate
- Tulis fungsi home di views.py yang mengembalikan render("home.html", context). 
- Atur routing di urls.py di direktori main dan include di urls.py direktori here_we_goods. 
- Buat home.html dan tampilkan nama aplikasi + nama & kelas.

2. ![penjelasan nomor 2](https://github.com/NalaWicaksono/here-we-goods/blob/master/bagan%20dan%20penjelasan%20file.jpg)

3. settings.py adalah pusat konfigurasi proyek. Di sini kita mendaftarkan aplikasi INSTALLED_APPS, menyusun middleware, mengatur sistem template, koneksi database, juga keamanan dasar seperti ALLOWED_HOSTS
4. Alur migrasi adalah: ubah model -> jalankan makemigrations untuk membuat file migrasi (berisi operasi skema) -> jalankan migrate agar operasi itu diterapkan ke database dan dicatat riwayatnya. 
5. Struktur MVT jelas → memisahkan data, logika, dan tampilan sehingga mudah dipahami pemula
6. menurut saya, tolong untuk kedepannya agar menyampaikan informasi yang penting mengenai tugas di awal. misalnya seperti informasi mengenai repo yang digunakan, di deskripsi tugas baru dijelaskan di akhir-akhir. menurut saya lebih baik disampaikan di awal agar tidak menimbulkan kebingungan
