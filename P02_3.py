kamar = int(input("Masukkan nomor kamar: "))
ruangmakan = kamar
while ruangmakan > 9 :
    jumlahdigit = 0
    # Menghitung total digit
    while ruangmakan > 9 :
        jumlahdigit += ruangmakan % 10
        ruangmakan = ruangmakan // 10
    jumlahdigit += ruangmakan
    ruangmakan = jumlahdigit

print(f"Kamar {kamar} akan termasuk ke dalam ruang makan {ruangmakan}")