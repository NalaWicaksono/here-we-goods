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


Tugas 3
1. Data delivery adalah proses mengirim data dari server ke klien dalam format terstruktur agar bisa diproses aplikasi lain. Kita memerlukan data delivery karena sebuah platform terdiri dari banyak bagian yang terpisah dan seringkali ditulis dalam teknologi yang berbeda, yang semuanya perlu berkomunikasi. Data delivery adalah jembatan yang memungkinkan komunikasi tersebut.

2. Menurut saya lebih bagus JSON karena lebih mudah dipahami dibanding XML. JSON lebih populer sekarang karena lebih cocok dengan API modern dan perangkat mobile. 

3. is_valid() menjalankan validasi sesuai tipe field/validator. Jika berhasil, ia mengisi form.cleaned_data yang aman dipakai (.save() atau logic lain). Tanpa ini, data tidak tervalidasi bisa masuk ke database (salah tipe, kosong, melanggar aturan).

4. csrf_token melindungi dari Cross-Site Request Forgery (CSRF), serangan yang memaksa browser pengguna mengirim request ke situs yang sedang login tanpa sepengetahuan mereka. jika tidak diterapkan, penyerang bisa membuat halaman jebakan yang men-trigger aksi (misalnya ubah data) memakai cookie sesi korban.

5. 
- Model: buat/cek Item (name, amount, description, opsional image), lalu makemigrations & migrate.

- Form: ItemForm. Jika ada gambar, pastikan template form pakai enctype="multipart/form-data".

- Views: show_items (list item), add_item (tambah item, cek is_valid()), item_detail (opsional, detail).

- Data Delivery: endpoint show_json, show_xml, show_json_by_id, show_xml_by_id (serialize QuerySet).

- URL: daftarkan routes di main/urls.py, lalu include('main.urls') di here_we_goods/urls.py.

- Templates: home.html, add_item.html, detail_item.html; selalu gunakan {% csrf_token %}.

6. Mungkin tambahkan cara troubleshooting masalah yang umum terjadi. kemarin saya sudah mengerjakan tutorial tapi hasilnya sempat error


Tugas 4
1. AuthenticationForm adalah form jadi untuk login bawaan django. Kita tinggal pakai untuk mengecek username dan password ke database.

Kelebihan:
- Praktis: langsung pakai tanpa bikin form sendiri.
- Aman: password dibandingkan dengan hash di database.

Kekurangan:
- Tampilannya polos dan kurang menarik

2. Simpelnya, Autentikasi adalah proses pengecekan pengguna (siapa yang sedang mengakses), biasanya dilakukan pada proses login, sedangkan otorisasi adalah pengecekan apakah pengguna berhak melakukan hal tertentu.

Di Django:
- Autentikasi: pakai model User, fungsi login() dan logout(), dan session.

- Otorisasi: pakai @login_required, permission, dan group.
Contoh paling sering: @login_required untuk membatasi halaman hanya bagi yang sudah login 

3. Kelebihan:
- cookies: Cocok untuk info ringan
- session: Lebih aman untuk data penting dan bisa lebih besar.

Kekurangan:
- cookies: Bisa diutak-atik user, kapasitas kecil, perlu pengamanan
- session: Menambah beban penyimpanan di server.

4. Belum tentu aman. Ada risiko dicuri/dibajak (XSS, session hijacking), CSRF, atau dimanipulasi.

Mitigasi yang disarankan:
- Pasang atribut HttpOnly, Secure, SameSite.
- Jangan taruh data rahasia di cookie.
- Aktifkan perlindungan CSRF bawaan Django.
- Gunakan HTTPS.

5. - menambahkan fungsi register dan login lalu menambahkan kode pada file html login.html dan register.html
- merestriksi dengan menambahkan @login_required pada beberapa fungsi
- membuat fungsi logout dan menambahkan tombol logout di main page
- Hubungkan data dengan user dengan menambahkan field user = models.ForeignKey(User, ...) pada model 
- manambahkan routing di urls.py


Tugas 5
1. Urutan kekuatan aturan: inline style → ID # → class ./attribute/pseudo-class → tag elemen/pseudo-elemen. Jika levelnya sama, aturan yang muncul paling akhir di CSS menang. (Catatan: !important bisa mengalahkan urutan normal, tapi gunakan hemat.)

2. Satu basis kode untuk berbagai ukuran layar membuat tampilan konsisten, aksesibilitas lebih baik, dan tidak perlu situs versi mobile terpisah. Uji cepat dengan Toggle Device Mode di DevTools untuk melihat breakpoints dan perilaku layout.\

3. Padding: ruang di dalam border (antara konten dan border).
Border: garis tepi elemen.
Margin: ruang di luar border, memisahkan elemen dari elemen lain.

4. Flexbox: tata letak 1 dimensi (baris atau kolom) dan alignment fleksibel.
CSS Grid: tata letak 2 dimensi (baris dan kolom) yang pas untuk kerangka halaman/katalog.

5. 
a. Siapkan styling
- Aktifkan static files & tambahkan Tailwind via CDN di base.html.
- Tambah static/css/global.css untuk gaya form + override dark mode (termasuk autofill).

b. Layout dasar
- Buat base.html bertema gelap (slate) dengan aksen violet.
- Buat navbar.html responsif + hamburger. Pastikan semua link pakai namespace main:.

c. Model & form
- Gunakan model Product (name, price, description, thumbnail, category, is_featured, user).
- Pakai ProductForm untuk tambah/edit.

d. Routing & views (CRUD Product)
- '' → product_list (home).
- products/new/ → product_create.
- products/<int:pk>/ → product_detail.
- products/<int:pk>/edit/ → product_edit.
- products/<int:pk>/delete/ → product_delete.


e. Template halaman
- Home (home.html): grid card responsif (1/2/3 kolom), tombol Detail/Edit/Delete, tombol filter All/My, 
- Detail (detail_product.html): tampilkan foto produk besar di atas, harga, deskripsi, dan aksi.
- Add/Edit (add_product.html / edit_product.html): card gelap + kelas .dark-form, tombol ungu.
- Auth (login.html/register.html): kotak gelap, input/placeholder terang, 

Tugas 6
1. Synchronous (full-page)

Cara kerja: browser mengirim form → server merender HTML lengkap → browser memuat ulang seluruh halaman.

Asynchronous (AJAX: fetch/XHR)

Cara kerja: JavaScript mengirim request di background (umumnya JSON). Sambil menunggu, UI tetap hidup (bisa tampil loading).

2. 
- Event di UI (klik tombol “Publish”, “Login”) memicu fetch() / FormData.

- Kirim request (POST/PUT/DELETE/GET) + CSRF token (header X-CSRFToken) ke endpoint, mis: /api/products/ atau /api/auth/login/.

- URLconf Django memetakan ke view.

- View memproses:

1. Validasi pakai Form/ModelForm atau authenticate().

2. Akses DB (create/update/delete/query).

3. Balikkan JsonResponse + HTTP status yang tepat (201/200/400/404).

- Frontend membaca JSON → update DOM (tutup modal, render kartu, tampilkan toast, refresh list) tanpa reload.

3. 
- UX jauh lebih cepat (hanya data yang perlu dikirim/diterima, bukan seluruh HTML).

- Tanpa reload → state halaman (scroll, tab yang sedang aktif, input lain) tetap terjaga.

- Interaksi halus: modal, inline validation, loading/empty/error state, toast.

- Hemat bandwidth: kirim JSON kecil, bukan template penuh.

4. 
- Gunakan HTTPS selalu (lindungi kredensial & cookie).

- CSRF protection: sertakan token ({% csrf_token %}), kirim via header X-CSRFToken. Jangan mem-bypass dengan @csrf_exempt.

- Kredensial hanya via POST; jangan pernah lewat GET / querystring.

5. 
- Perceived performance lebih cepat → rasa seperti app.

- Alur kerja mulus: modal CRUD, filter cepat, hasil muncul instan.

- jika gagal jaringan, tampilkan retry, kita sudah punya tombol “Refresh” & “Coba lagi” tanpa harus refresh di browser