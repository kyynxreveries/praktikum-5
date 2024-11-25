DAFTAR ISI
==========
- [LAPORAN PRAKTIKUM 5](#laporan-praktikum-5)   
    - [CODE PROGRAM DAFTAR NILAI](#code-program-daftar-nilai)
    - [FLOWCHART DAFTAR NILAI](#flowchart-daftar-nilai)
    - [KESIMPULAN](#kesimpulan)

# LAPORAN PRAKTIKUM 5


## CODE PROGRAM DAFTAR NILAI

### Step 1 : Inisialisasi Data
Tambahkan variabel data_nilai sebagai list kosong yang digunakan untuk menyimpan data mahasiswa, setiap elemen dalam list adalah dictionary yang berisi informasi mahasiswa, 
seperti NIM, Nama, Nilai Tugas, Nilai UTS, Nilai UAS, dan Nilai Akhir yang akan diinputkan :

![1 (1)](https://github.com/user-attachments/assets/ef32e9a2-3538-4701-9080-7d4e0e9ad626)

### Step 2 : Fungsi lihat_data
Fungsi ini digunakan untuk menampilkan daftar nilai mahasiswa :
- Jika data_nilai kosong, akan muncul pesan "Tidak Ada Data Mahasiswa".
- Jika data_nilai berisi data, ditampilkan dalam bentuk tabel, tabel akan berisikan data yang sudah diinputkan oleh user NIM, Nama, Nilai Tugas, Nilai UTS, Nilai UAS, dan Nilai Akhir.

![2](https://github.com/user-attachments/assets/47c04c03-353c-4e23-b768-09d3bbd45a26)

### Step 3 : Fungsi tambah_data
Fungsi ini digunakan untuk menambahkan data nilai mahasiswa ke dalam data_nilai. Langkah-langkahnya, Meminta input dari pengguna untuk NIM, Nama, Nilai Tugas, Nilai UTS, dan Nilai UAS, menghitung nilai akhir dengan bobot (Tugas: 30%, UTS: 35%, UAS: 35%), menambahkan data mahasiswa dalam bentuk dictionary ke list data_nilai. Perintah .append berfungsi untuk menambahkan data/memasukan tambahan data baru ke yang sudah disediakan :

![3 (1)](https://github.com/user-attachments/assets/56f764e6-76e7-4265-856d-61b3ac4931b2)

### Step 4 : Fungsi ubah_data
Fungsi ini digunakan untuk mengubah data mahasiswa berdasarkan nomor yang dipilih menampilkan data mahasiswa dengan lihat_data serta meminta pengguna memilih nomor data yang ingin diubah, hal ini mencakup semua data dari NIM, Nama, Nilai Tugas, Nilai UTS, dan Nilai UAS yang diubah, namun ada 2 kondisi dalam kasus ini :
- Jika nomor tidak valid, tampilkan pesan "Data tidak ditemukan".
- Jika valid, memperbarui data dengan input baru.

![4](https://github.com/user-attachments/assets/cca210df-d5d4-417b-8550-087939eaf72e)

### Step 5 : Fungsi hapus_data
Fungsi ini menghapus data mahasiswa dari data_nilai yang sudah tercantumkan datanya pada tabel. outputnya akan menampilkan daftar data dan meminta nomor data yang akan dihapus. 
Jika nomor valid, data dihapus dengan del :

![5 (1)](https://github.com/user-attachments/assets/cfd5b06e-73aa-4040-a395-9ba3ff3f4d9e)


### Step 6 : Fungsi cari_data
Fungsi ini mencari data mahasiswa berdasarkan nama yang sudah tertera/data pada tabel data dengan menggunakan list comprehension untuk mencari nama yang cocok (case-insensitive), jika ditemukan akan menampilkan data mahasiswa jika tidak, menampilkan pesan "Data tidak ditemukan" :

![6](https://github.com/user-attachments/assets/15bd6265-bfb0-4c6a-a6b6-0ed716974b2e)


### Step 7 : Main Loop
Loop ini merupakan antarmuka utama program selanjutnya akan menampilkan menu pilihan berdasarkan input pengguna, pilihannya yaitu:
- L: Memanggil lihat_data.
- T: Memanggil tambah_data.
- U: Memanggil ubah_data.
- H: Memanggil hapus_data.
- C: Memanggil cari_data.
- K: Keluar dari program.

Jika input tidak valid, menampilkan pesan "Menu tidak valid".

![7](https://github.com/user-attachments/assets/17cbe1c4-eae3-4334-a223-4cc9c3405aaf)

### Step 8 : Run Program
Tahap akhir adalah uji coba code program yang sudah dibuat dengan mencoba berbagai kemungkinan yang ada.

![8](https://github.com/user-attachments/assets/c62e34b9-6b09-4db2-9bd2-2ee368c2b9f8)

### Step 9 : hasil akhir 

![WhatsApp Image 2024-11-25 at 09 45 33](https://github.com/user-attachments/assets/33c9aebe-24b1-488a-8d60-2804eddae978)

## FLOWCHART DAFTAR NILAI

![17 (1)](https://github.com/user-attachments/assets/2848a686-a3c9-4de6-b48c-23501f6510a2)

### Step 1 :
Titik mulai sebuah program atau alur.

### Step 2 :
lalu lakukan inisialisasi dengan menampilkan menu yang tersedia.

### Step 3 :
Inputkan code menu yang ingin dilakukan, setiap code berisi [L]ihat, [T]ambah, [U]bah, [H]apus, [C]ari, [K]eluar.

### Step 4 :
Dalam kasus ini semua kemgkinan dapat terjadi, kondisi yang diperlukan sesuai apa yang akan diinoutkan user.

- Jika [L]ihat, maka user akan di tampilkan sebuah tabel dari daftar nilai, namun jika tabel belum ada isi/kosong maka akan tampil tidak ada data, jika ada maka ditampilkan sebuah data nilai mahasiswa. Setelah tampilkan data maka akan kembali menuju inisialisasi menu. 

- Jika [T]ambah, user diminta memasukan sebuah data yang berupa :
    - NIM
    - Nama
    - Nilai Tugas
    - Nilai UTS
    - Nilai UAS

Lalu User akan diarahkan kembali ke inisialiasi menu.

- Jika [U]bah, sama dengan [L]ihat jika tidak ada data nilai maka akan tampil tidak ada data nilai namun [U]bah kalau ada data nilai user diminta menginputkan Nomor urut yang akan diubah, setelah itu diminta untuk mengisi atau menginputkan data valid yang diubah. Setelah itu user kembali ke inisialisasi menu.

- Jika [C]ari, user diminta memasukan nama yang dicari, setelah itu maka akan ditampilkan tabel daftar nilai mahasiswa. Setelah itu kembali ke inisialisasi menu.

- Jika [H]apus, user akan ditampilkan daftar nilai lalu diminta memasukan sebuah nomor yang ingin dihapus dari daftar. Setelah itu kembalu ke inisialisasi menu.

- jika [K]eluar, User akan keluar program dan program akan berhenti.

## KESIMPULAN
Dengan membuat code program daftar nilai ini saya pribadi dapat mengambil pelajaran, kita mampu membuat sebuah program sederhana untuk membuatkan list yang berisikan dictionary sebagai element yang membantu 
pada Laporan Praktikum kali ini. Selain itu, ada nya flowchart yang dibuat dengan banyak nya perulangan tapi tetap dengan konsep harus ada perhentian, karena sebuah program harus memiliki 
sebuah titik berhenti.
