import matplotlib.pyplot as plt
import numpy as np
import random
import math
import sys
sys.setrecursionlimit(20000)
# FUNGSI DAN PROSEDUR

# fungsi untuk mengurutkan titik-titik yang tersedia
def sort_titik(daftar_awal):
    daftar_titik = []
    while (len(daftar_awal) != 0):
        correct = False
        i = 0

        if len(daftar_titik) != 0:
            while not correct:
                if i == len(daftar_titik) or daftar_awal[0][0] <= daftar_titik[i][0]:
                    correct = True
                else:
                    i += 1

        daftar_titik.insert(i, daftar_awal[0])

        daftar_awal.remove(daftar_awal[0])
    return daftar_titik

# fungsi untuk membangi daftar titik kedalam bagian kiri dan kanan
def bagi_titik(daftar_awal, mid):
    titik_kiri = []
    titik_kanan = []

    for i in daftar_awal:
        if (i[0] < mid):
            titik_kiri.append(i)
        elif (i[0] > mid):
            titik_kanan.append(i)
        else:
            titik_kiri.append(i)
            titik_kanan.append(i)

    return titik_kiri, titik_kanan

# fungsi untuk membagi titik-titik dengan jarak delta dari sumbu gabungan 2 buah strip
def bagi_titik_delta(daftar_awal, mid, delta):
    daftar_titik = []

    for i in daftar_awal:
        if (i[0] <= mid and i[0] >= mid - delta) or (i[0] >= mid and i[0] <= mid + delta):
            daftar_titik.append(i)

    return daftar_titik

# fungsi untuk mencari jumlah titik di strip
def jumlah_titik_di_strip(daftar_titik, xkiri, xkanan):
    ctr = 0
    for i in daftar_titik:
        if i[0] >= xkiri and i[0] <= xkanan:
            ctr += 1
            
    return ctr

# fungsi untuk mencari tahu apakah seluruh titik pada strip merupakan titik yang sama
def titik_di_strip_sama(daftar_titik):
    sama = True
    i = len(daftar_titik)
    ctr = 0

    while sama and ctr < i:
        if daftar_titik[0] != daftar_titik[ctr]:
            sama = False
        else:
            ctr += 1
    return sama

# fungsi untuk mencari jarak euclidean
def euclidean_distance(titik1, titik2):
    temp = 0
    for i in range(len(titik1)):
        temp += pow(titik1[i] - titik2[i], 2)

    return math.sqrt(temp)

# fungsi untuk mencari minimum distance khusus untuk titik-titik pada area gabungan
def find_minimum_combined(daftar_titik, delta):
    jumlah = len(daftar_titik)
    if jumlah == 2:
        return daftar_titik[0], daftar_titik[1], euclidean_distance(daftar_titik[0], daftar_titik[1])
    elif jumlah == 3:
        jarak1 = euclidean_distance(daftar_titik[0], daftar_titik[1])
        jarak2 = euclidean_distance(daftar_titik[0], daftar_titik[2])
        jarak3 = euclidean_distance(daftar_titik[1], daftar_titik[2])

        if jarak1 <= jarak2 and jarak1 <= jarak3:
            return daftar_titik[0], daftar_titik[1], jarak1
        elif jarak2 <= jarak1 and jarak2 <= jarak3:
            return daftar_titik[0], daftar_titik[2], jarak2
        else:
            return daftar_titik[1], daftar_titik[2], jarak3
    else:
        


# fungsi rekursif untuk mencari minimum distance dengan metode divide and conquer
def find_minimum(daftar_titik, xkiri, xkanan, ctr_euclidean):
    jumlah = jumlah_titik_di_strip(daftar_titik, xkiri, xkanan)
    # basis
    # jika jumlah titik di strip 1/2/3
    if jumlah == 0:
        return None, None, None
    elif jumlah == 1:
        return None, None, None
    elif jumlah == 2:
        ctr_euclidean += 1
        return daftar_titik[0], daftar_titik[1], euclidean_distance(daftar_titik[0], daftar_titik[1])
    elif jumlah == 3:
        ctr_euclidean += 3
        jarak1 = euclidean_distance(daftar_titik[0], daftar_titik[1])
        jarak2 = euclidean_distance(daftar_titik[0], daftar_titik[2])
        jarak3 = euclidean_distance(daftar_titik[1], daftar_titik[2])

        if jarak1 <= jarak2 and jarak1 <= jarak3:
            return daftar_titik[0], daftar_titik[1], jarak1
        elif jarak2 <= jarak1 and jarak2 <= jarak3:
            return daftar_titik[0], daftar_titik[2], jarak2
        else:
            return daftar_titik[1], daftar_titik[2], jarak3
    # rekursi
    # jika jumlah titik di strip > 3
    else:
        if (titik_di_strip_sama(daftar_titik)):
            return daftar_titik[0], daftar_titik[1], 0
        else:
            distance = (xkanan - xkiri/2)
            daftar_titik_kiri, daftar_titik_kanan = bagi_titik(daftar_titik, xkiri+distance)
            titik_kiri_1, titik_kiri_2, delta_kiri = find_minimum(daftar_titik_kiri, xkiri, xkiri+distance, ctr_euclidean)
            titik_kanan_1, titik_kanan_2, delta_kanan = find_minimum(daftar_titik_kanan, xkiri+distance, xkanan, ctr_euclidean)

            if delta_kanan is not None and delta_kiri is not None:
                # gabungkan
                daftar_titik_gabungan = bagi_titik_delta(daftar_titik, xkiri+distance, min(delta_kiri, delta_kanan))

                if (len(daftar_titik_gabungan) > 1) :
                    # eksekusi fungsi mencari jarak khusus untuk titik gabungan

                else:
                    if delta_kanan < delta_kiri:
                        return titik_kanan_1, titik_kanan_2, delta_kanan
                    else:
                        return titik_kiri_1, titik_kiri_2, delta_kiri
            else:
                if xkanan is None:
                    return titik_kiri_1, titik_kiri_2, delta_kiri
                else:
                    return titik_kanan_1, titik_kanan_2, delta_kanan

            # # jika ada satu saja yang bernilai jumlah titiknya "null" maka skip
            # if delta_kiri != "null" and delta_kanan != "null":
            #     daftar_titik_gabungan = bagi_titik_delta(daftar_titik, xkiri+distance, min(delta_kiri, delta_kanan))
                
            #     # penggabungan
            #     if len(daftar_titik_gabungan) > 1:
            #         for i in range(len(daftar_titik_gabungan)-1):
            #             for j in range(i+1, len(daftar_titik_gabungan)):
            #                 temp = euclidean_distance(daftar_titik_gabungan[i], daftar_titik_gabungan[j])
            #                 if i == 0 and j == 1:
            #                     combined_distance = temp
            #                     titik_gabungan_1 = daftar_titik_gabungan[i]
            #                     titik_gabungan_2 = daftar_titik_gabungan[j]
            #                 else:
            #                     if combined_distance > temp:
            #                         combined_distance = temp
            #                         titik_gabungan_1 = daftar_titik_gabungan[i]
            #                         titik_gabungan_2 = daftar_titik_gabungan[j]

            #         if combined_distance < min(delta_kiri, delta_kanan):
            #             return titik_gabungan_1, titik_gabungan_2, combined_distance
            #         else:
            #             if delta_kiri < delta_kanan:
            #                 return titik_kiri_1, titik_kiri_2, delta_kiri
            #             else:
            #                 return titik_kanan_1, titik_kanan_2, delta_kanan
            #     else:
            #         return "null", "null", "null"
            # else:
            #     if delta_kiri == "null" and delta_kanan == "null":
            #         return "null", "null", "null"
            #     else:
            #         if delta_kiri != "null":
            #             return titik_kiri_1, titik_kiri_2, delta_kiri
            #         else:
            #             return titik_kanan_1, titik_kanan_2, delta_kanan 

# fungsi untuk mencari minimum distance dengan metode bruteforce
def find_minimum_bruteforce(daftar_titik):
    for i in range(len(daftar_titik)-1):
        for j in range(i+1, len(daftar_titik)):
            if i == 0 and j == 1:
                temp = euclidean_distance(daftar_titik[i], daftar_titik[j])
                titik_1 = daftar_titik[i]
                titik_2 = daftar_titik[j]
            else:
                if temp > euclidean_distance(daftar_titik[i], daftar_titik[j]):
                    temp = euclidean_distance(daftar_titik[i], daftar_titik[j])
                    titik_1 = daftar_titik[i]
                    titik_2 = daftar_titik[j]
    
    return titik_1, titik_2, temp

# PROGRAM UTAMA
def main():
    # inisialisasi
    fig = plt.figure(figsize=plt.figaspect(0.5))
    ax = fig.add_subplot(1, 2, 1, projection='3d')
    bx = fig.add_subplot(1, 2, 2, projection='3d')

    n = int(input("Masukkan jumlah titik: "))
    x = []
    dimensi = 3

    for i in range(n):
        temp = []
        for j in range(dimensi):
            temp.append(random.randint(-100, 100))
        x.append(temp)

    # sort terlebih dahulu titik"nya
    daftar_titik = sort_titik(x)
    print(daftar_titik)

    # algoritma disini
    jumlahperhitungan = 0
    pasangan1, pasangan2, jarak = find_minimum(daftar_titik, daftar_titik[0][0], daftar_titik[len(daftar_titik)-1][0], jumlahperhitungan)
    print(jarak)
    print(pasangan1)
    print(pasangan2)

    # algoritma bruteforce
    pasangan_brute_1, pasangan_brute_2, jarak_brute = find_minimum_bruteforce(daftar_titik)
    print(jarak_brute)
    print(pasangan_brute_1)
    print(pasangan_brute_2)


    

    # masukkan ke figur
    for i in daftar_titik:
        if i == pasangan1 or i == pasangan2:
            ax.scatter(i[0], i[1], i[2], c ='g', marker='o')
        else:
            ax.scatter(i[0], i[1], i[2], c ='r', marker='o')

    for i in daftar_titik:
        if i == pasangan_brute_1 or i == pasangan_brute_2:
            bx.scatter(i[0], i[1], i[2], c ='g', marker='o')
        else:
            bx.scatter(i[0], i[1], i[2], c ='b', marker='o')
            
    plt.show()

if __name__ == "__main__":
    main()