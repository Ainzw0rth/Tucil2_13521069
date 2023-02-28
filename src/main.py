import matplotlib.pyplot as plt
import numpy as np
import random
import math
import time
import sys
sys.setrecursionlimit(20000)

# FUNGSI DAN PROSEDUR

# fungsi untuk menyalin daftar titik
def copy_titik(daftar_awal):
    daftar_awal_copy = []
    for i in daftar_awal:
        daftar_awal_copy.append(i)

    return daftar_awal_copy

# fungsi untuk mengurutkan titik-titik yang tersedia
def sort_titik(daftar_awal, based_on):
    daftar_awal_copy = copy_titik(daftar_awal)

    daftar_titik = []
    while (len(daftar_awal_copy) != 0):
        correct = False
        i = 0

        if len(daftar_titik) != 0:
            while not correct:
                if i == len(daftar_titik) or daftar_awal_copy[0][based_on] <= daftar_titik[i][based_on]:
                    correct = True
                else:
                    i += 1

        daftar_titik.insert(i, daftar_awal_copy[0])

        daftar_awal_copy.remove(daftar_awal_copy[0])
    return daftar_titik

# fungsi untuk mencari jarak euclidean
def euclidean_distance(titik1, titik2):
    temp = 0
    for i in range(len(titik1)):
        temp += pow(titik1[i] - titik2[i], 2)

    return math.sqrt(temp)

# fungsi untuk membagi titik-titik pada daftar titik menjadi 2 buah daftar titik baru yang berisikan titik di sebelah kiri dan di sebelah kanan
def bagi_titik(daftar_awal):
    daftar_kiri = []
    daftar_kanan = []

    mid = len(daftar_awal) // 2
    mid_point = daftar_awal[mid]

    for i in range(len(daftar_awal)):
        if (daftar_awal[i][0] <= mid_point[0]):
            daftar_kiri.append(daftar_awal[i])
        else:
            daftar_kanan.append(daftar_awal[i])

    return daftar_kiri, daftar_kanan

# fungsi untuk mendapatkan titik-titik yang berada di sekitar batas penggabungan 2 buah area
def bagi_titik_gabungan(daftar_awal, delta):
    titik_gabungan = []

    mid = len(daftar_awal) // 2
    mid_point = daftar_awal[mid]

    for i in range(len(daftar_awal)):
        if (daftar_awal[i][0] <= mid_point[0] + delta) and (daftar_awal[i][0] >= mid_point[0] - delta):
            titik_gabungan.append(daftar_awal[i])

    return titik_gabungan

# fungsi untuk mencari titik

def find_minimum(daftar_titik, counter):
    if (len(daftar_titik) == 1):
        return None, None, counter
    elif (len(daftar_titik) == 2):
        return [[daftar_titik[0], daftar_titik[1]]], euclidean_distance(daftar_titik[0], daftar_titik[1]), counter+1
    elif (len(daftar_titik) == 3):
        jarak1 = euclidean_distance(daftar_titik[0], daftar_titik[1])
        jarak2 = euclidean_distance(daftar_titik[0], daftar_titik[2])
        jarak3 = euclidean_distance(daftar_titik[1], daftar_titik[2])
        if jarak1 == min(jarak1, jarak2, jarak3):
            return [[daftar_titik[0], daftar_titik[1]]], jarak1, counter+3
        elif jarak2 == min(jarak1, jarak2, jarak3):
            return [[daftar_titik[0], daftar_titik[2]]], jarak2, counter+3
        else:
            return [[daftar_titik[1], daftar_titik[2]]], jarak3, counter+3
    else:
        daftar_titik_kiri, daftar_titik_kanan = bagi_titik(daftar_titik)
        # tidak bisa dibagi lagi
        if (daftar_titik_kiri == daftar_titik):
            return find_minimum_gabungan(daftar_titik, counter)
        else:
            titik_kiri, delta_kiri, counter = find_minimum(daftar_titik_kiri, counter)
            titik_kanan, delta_kanan, counter = find_minimum(daftar_titik_kanan, counter)

            if delta_kanan is None or delta_kiri is None:
                if delta_kanan is None and delta_kiri is None:
                    return None, None, None, counter
                else:
                    if delta_kanan is None:
                        return titik_kiri, delta_kiri, counter
                    else:
                        return titik_kanan, delta_kanan , counter
            else:
                delta = min(delta_kanan, delta_kiri)
                # gabung 
                daftar_titik_gabungan = bagi_titik_gabungan(daftar_titik, delta)

                if len(daftar_titik_gabungan) > 1:
                    titik_gabungan, delta_gabungan, counter = find_minimum_gabungan(daftar_titik_gabungan, counter)

                    if delta_gabungan is not None:
                        if delta_gabungan < delta:
                            return titik_gabungan, delta_gabungan, counter
                        elif delta_gabungan == delta:
                            if delta_kanan > delta_kiri:
                                for i in titik_gabungan:
                                    if i not in titik_kiri:
                                        titik_kiri.append(i)
                                return titik_kiri, delta_kiri, counter
                            elif delta_kanan < delta_kiri:
                                for i in titik_gabungan:
                                    if i not in titik_kanan:
                                        titik_kanan.append(i)
                                return titik_kanan, delta_kanan, counter
                            else:
                                for i in titik_gabungan:
                                    if i not in titik_kanan:
                                        titik_kanan.append(i)
                                for i in titik_kiri:
                                    if i not in titik_kanan:
                                        titik_kanan.append(i)
                                return titik_kanan, delta_kanan, counter
        
                if delta_kanan > delta_kiri:
                    return titik_kiri, delta_kiri, counter
                elif delta_kanan == delta_kiri:
                    for i in titik_kiri:
                        if i not in titik_kanan:
                            titik_kanan.append(i)
                    return titik_kanan, delta_kanan, counter
                else:
                    return titik_kanan, delta_kanan, counter


# fungsi untuk mencari minimum distance dengan metode bruteforce
def find_minimum_gabungan(daftar_titik, counter):
    min = euclidean_distance(daftar_titik[0], daftar_titik[1])
    titik_gabungan = [[daftar_titik[0], daftar_titik[1]]]
    counter += 1

    for i in range(len(daftar_titik)-1):
        for j in range(i+1, len(daftar_titik)):
            if i != 0 and j != 1:
                counter += 1
                temp = euclidean_distance(daftar_titik[i], daftar_titik[j])
                if min > temp:
                    min = temp
                    titik_gabungan = [[daftar_titik[i], daftar_titik[j]]]
                elif min == temp:
                    if [daftar_titik[i], daftar_titik[j]] not in titik_gabungan:
                        titik_gabungan.append([daftar_titik[i], daftar_titik[j]])
                    
    return titik_gabungan, min, counter

# fungsi untuk menjadikan seluruh solusi titik menjadi sebuah string
def solution_to_string(daftar_solusi, dimensi):
    temp = ""
    warna = ["merah", "ungu", "coklat", "merah muda", "abu-abu", "olive", "cyan", "oranye", "hitam"]
    color_cycle = 0

    for i in daftar_solusi:
        if dimensi == 3:
            temp += (f"- Titik {i[0]} dengan titik {i[1]}\n  diwarnai dengan warna: {warna[color_cycle % 9]}\n")
            color_cycle+=1
        else:
            temp += (f"- Vektor {i[0]} dengan vektor {i[1]}\n")

    return temp

# PROGRAM UTAMA
def main():
    # inisialisasi
    fig = plt.figure(figsize=(15, 9))
    ax = fig.add_subplot(2, 3, 1, projection='3d')
    bx = fig.add_subplot(2, 3, 3, projection='3d')
    ax.set_title("Hasil dari Divide and Conquer")
    bx.set_title("Hasil dari Bruteforce")
    n = int(input("Masukkan jumlah titik: "))
    while n < 2:
        n = int(input("Jumlah titik minimal 2, masukkan lagi jumlah titik: "))
    dimensi = int(input("Masukkan dimensi (note: visualisasi hanya akan diberikan untuk dimensi 3, selain itu hanya sebatas di terminal):\n"))
    while dimensi < 1:
        dimensi = int(input("Jumlah dimensi minimal 1, masukkan lagi jumlah dimensi: "))

    x = []

    lowerbound = float(input("Masukkan batas bawah nilai titik (note: maksimal -1000): "))
    upperbound = float(input("Masukkan batas atas nilai titik (note: maksimal 1000): "))
    while (upperbound <= lowerbound):
        print("Masukan salah!! batas bawah harus lebih kecil dari batas atas")
        lowerbound = float(input("Masukkan batas bawah nilai titik (note: maksimal -1000): "))
        upperbound = float(input("Masukkan batas atas nilai titik (note: maksimal 1000): "))
    for i in range(n):
        temp = []
        for j in range(dimensi):
            temp.append(round(random.uniform(lowerbound, upperbound), 3))
        x.append(temp)

    # sort terlebih dahulu titik"nya
    daftar_titik = sort_titik(x, 0)

    #print(daftar_titik)

    # algoritma disini
    jumlahperhitungan_divide = 0
    start_divide = time.time()
    pasangan_divide, jarak, jumlahperhitungan_divide = find_minimum(daftar_titik, jumlahperhitungan_divide)
    end_divide = time.time()
    exec_time_divide = end_divide-start_divide
    
    info_divide = f"Deskripsi hasil Divide and Conquer:\n\nWaktu eksekusi: {exec_time_divide}s \nJumlah kalkulasi: {jumlahperhitungan_divide}\nJarak terdekat: {jarak}\nSolusi:\n{solution_to_string(pasangan_divide, dimensi)}"
    ax.text2D(0.1, 0.1, info_divide, fontsize=9, transform=plt.gcf().transFigure)

    # algoritma bruteforce
    jumlahperhitungan_brute = 0
    start_brute = time.time()
    pasangan_brute, jarak_brute, jumlahperhitungan_brute = find_minimum_gabungan(daftar_titik, jumlahperhitungan_brute)
    end_brute = time.time()
    exec_time_brute = end_brute-start_brute

    info_brute = f"Deskripsi hasil Bruteforce:\n\nWaktu eksekusi: {exec_time_brute}s \nJumlah kalkulasi: {jumlahperhitungan_brute}\nJarak terdekat: {jarak_brute}\nSolusi:\n{solution_to_string(pasangan_brute, dimensi)}"
    bx.text2D(0.6, 0.1, info_brute, fontsize=9, transform=plt.gcf().transFigure)

    # semua data akan ditampilkan di terminal 
    print(f"\nTitik yang digunakan: {x}\n")
    print(info_divide)
    print("\n")
    print(info_brute)

    # VISUALISASI
    warna = ["red", "purple", "brown", "pink", "gray", "olive", "cyan", "orange", "black"]
    if dimensi == 3: # visualisasi hanya untuk dimensi 3
        for i in daftar_titik:
            ax.scatter(i[0], i[1], i[2], c ='g', marker='o')

        color_cycle = 0
        for i in pasangan_divide:
            ax.scatter(i[0][0], i[0][1], i[0][2], c = warna[color_cycle % 9], marker='o')
            ax.scatter(i[1][0], i[1][1], i[1][2], c = warna[color_cycle % 9], marker='o')
            color_cycle+=1

        for i in daftar_titik:
            bx.scatter(i[0], i[1], i[2], c ='b', marker='o')
        
        color_cycle = 0
        for i in pasangan_divide:
            bx.scatter(i[0][0], i[0][1], i[0][2], c = warna[color_cycle % 9], marker='o')
            bx.scatter(i[1][0], i[1][1], i[1][2], c = warna[color_cycle % 9], marker='o')
            color_cycle+=1
    
        plt.show()

if __name__ == "__main__":
    main()