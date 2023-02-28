# Tugas Kecil 2 Strategi Algoritma - IF2211

Program mencari pasangan titik dengan jarak terpendek pada ruang 3D dalam bahasa Python dan menggunakan algoritma Divide and Conquer

## Installing / Getting started
Program memerlukan: 
- python atau python3, untuk instalasi bisa dilihat di: https://www.python.org/downloads/
- matplotlib, untuk instalasi bisa dilihat di: https://matplotlib.org/stable/users/installing/index.html

## How to run?
Pertama-tama clone dulu repository ini, caranya adalah dengan membuka terminal pada folder dimana kalian mau programnya diclone. Setelah terminal dibuka maka masukan command ini ke terminal:

```shell
git clone https://github.com/Ainzw0rth/Tucil2_13521069.git
```

Setelah repositorynya diclone, buka terminal pada folder repositorynya dan lakukan command-command berikut untuk memindahkan ke directorynya:

```shell
cd src
```

Untuk menjalankan programnya, maka bisa dilakukan dengan memasukkan command berikut:

```shell
python main.py
```
atau jika matplotlib diinstall melalui python3
```shell
python3 main.py
```

## How to use?
Pertama-tama kita akan memasukkan n (jumlah titik) yang ingin kita gunakan. Jumlah titik yang dimasukkan minimal 2, jika memasukkan jumlah titik dibawah 2 maka program akan meminta input ulang.

Kemudian kita dapat memasukkan dimensi dari titik-titik tersebut. Dimensi yang valid adalah yang bernilai >= 1, jika yang dimasukkan adalah selain itu maka program akan meminta input ulang.

Kemudian kita dapat memasukkan batas bawah dan batas atas. Batas atas haruslah bernilai lebih besar daripada batas bawah, jika yang dimasukkan adalah selain itu maka program akan meminta input ulang. Untuk jaga-jaga janganlah memasukkan batas bawah yang bernilai lebih kecil dari -1000 atau batas atas yang bernilai lebih besar dari 1000, namun jika ingin mencoba program akan mengizinkannya.

Titik-titik yang digunakan serta solusi dari daftar titik tersebut akan ditampilkan di terminal. Khusus untuk dimensi 3, maka program akan secara otomatis membuka window baru yang berisi visualisasi dari solusi yang didapat. Kedua penampilan solusi tersebut akan disertai oleh solusi jika menggunakan metode bruteforce, hasil tersebut dapat dijadikan sebagai komparasi antar kedua algoritma.

## Made by
Louis Caesa Kesuma (13521069)