tinggi = int(input("Masukkan ketinggian awal bola: "))
tipe = int(input("Masukkan tipe bola: "))
pantul = 0
while tinggi > tipe :
    pantul += 1
    tinggi = tinggi / tipe

print(f"Bola akan memantul sebanyak {pantul} kali")