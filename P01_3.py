# Input bagian minuman
bagsusu = int(input("Masukkan bagian susu: "))
bagsirup = int(input("Masukkan bagian sirup: "))
bages = int(input("Masukkan bagian es: "))
mlperporsi = int(input("ml per porsi:"))

# Menghitung pembilang minuman
totalbagian = bagsirup + bagsusu + bages

# Bahan yang diperlukan untuk 1 porsi (dalam mL)
susuperporsi = mlperporsi / totalbagian * bagsusu
sirupperporsi = mlperporsi / totalbagian *bagsirup
esperporsi = mlperporsi / totalbagian * bages

#Bahan yang dimiliki
banyaksusu = int(input("Masukkan ml banyak susu: "))  
banyaksirup = int(input("Masukkan ml banyak sirup: "))  
banyakes = int(input("Masukkan ml banyak es: "))

# Jumlah minuman maksimal yang bisa dibuat menggunakan bahan yang tersedia
porsimaxsusu = banyaksusu // susuperporsi
porsimaxsirup = banyaksirup // sirupperporsi
porsimaxes = banyakes // esperporsi

# Maksimal minuman yang bisa dibuat
if porsimaxsusu < porsimaxsirup :
    if porsimaxsusu < porsimaxes :
        print(f"Jumlah minuman yang bisa dibuat {int(porsimaxsusu)} porsi")
    else :
        print(f"Jumlah minuman yang bisa dibaut {int(porsimaxes)} porsi")
else :
    if porsimaxsirup < porsimaxes :
        print(f"Jumlah minuman yang bisa dibuat {int(porsimaxsirup)} porsi")
    else :
        print(f"Jumlah minuman yang bisa dibaut {int(porsimaxes)} porsi")    