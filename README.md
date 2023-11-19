# SangkuLens: Sistem Temu Balik Gambar dengan CBIR
Menggunakan Aljabar Vektor untuk Content-Based Image Retrieval berdasarkan Parameter Warna dan Tekstur

##  Informasi Umum
Sistem temu balik gambar dapat dilakukan dengan  memanfaatkan Aljabar Vektor, melakukan komparasi dengan cosine similarity (memanfaatkan dot product dan panjang vektor) nilai-nilai vektor fitur gambar baik tekstur maupun warna. Aljabar vektor digunakan untuk menggambarkan dan menganalisis data menggunakan pendekatan klasifikasi berbasis konten (Content-Based Image Retrieval atau CBIR). Website dibuat untuk kemudahan pengguna dalam melakukan komparasi atau temu balik gambar.

## Teknologi yang Digunakan
Python
Flask
ReactJS

## Fitur
1. Mendapatkan gambar-gambar paling mirip dengan query image dengan perbandingan fitur warna
2. Mendapatkan gambar-gambar paling mirip dengan query image dengan perbandingan fitur tekstur

## Setup dan Penggunaan program
Clone repository ini ke lokal anda
<pre>
https://github.com/slntkllr01/Algeo02-22035.git
</pre>

1. Buka folder src
2. Buatlah virtual environment `venv` baru pada folder tersebut.
3. Aktifkan virtual environment tersebut `venv/bin/activate` di Linux/OS X ataupun `venv\scripts\activate` pada Windows.
4. Install dependensi yang diperlukan dengan `pip install -r requirements.txt`.
5. Kemudian, dengan terminal code editor Anda, masuk ke direktori app dengan `cd app`
6. Pastikan anda telah menginstal npm atau dengan `npm install`
7. Lalu bukalah website dengan `npm run start` untuk menjalankan program dari local browser
8. Pada terminal lain, jalankan juga  `npm run start-api` agar program dapat digunakan
9. Selamat mencoba!
   
## Cara Penggunaan Website
Secara umum, berikut adalah cara umum penggunaan program:
1. Pengguna memasukkan gambar yang ingin dicari dengan menekan tombol ‘Upload File’, setelah memilih, pengguna menekan tombol ‘Insert Image’
2. Kemudian, pengguna memasukkan multifiles gambar-gambar dataset yang ingin dicari dengan menekan tombol ‘Upload File’, setelah memilih, pengguna menekan tombol ‘Upload Dataset’
3. Pilih opsi pencarian, ini dapat dilakukan dengan menge-switch ingin melakukan pencarian berdasarkan warna atau tekstur.
4. Tekan tombol search, program kemudian akan memproses, mencari gambar-gambar dari dataset yang memiliki kemiripan dengan gambar yang dimasukkan tadi.
5. Program akan menampilkan kumpulan gambar yang mirip, diurutkan dari yang memiliki kemiripan paling tinggi ke yang paling rendah dan juga memunculkan persentase kemiripannya. 
6. Pengguna juga dapat melihat informasi terkait jumlah gambar yang muncul, dan waktu eksekusi programnya.

## Ruang Pengembangan
Tentu banyak hal yang bisa dikembangkan untuk tugas penulis, misalnya dalam hal kecepatan pemrosesan gambar. Tugas juga bisa lebih baik jika dilengkapi kemampuan menangkap gambar dari kamera, mengambil gambar dengan scraping, ataupun mengunduh hasil pemrosesan. Hal tersebut tentu dapat dikembangkan lebih jauh lagi dan semoga dapat penulis pelajari dan eksplorasi di kesempatan lain.

## Kontributor
1. 13522035 Melati Anggraini
2. 13522046 Raffael Boymian Siahaan
3. 13522087 Shulha
