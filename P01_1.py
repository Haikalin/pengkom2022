print("Keadaan awal: ")
jam = int(input("Jam: "))
menit = int(input("Menit: "))
detik = int(input("Detik: "))
mode  = input("Mode: ")
num = int(input("Nilai perubahan: "))
if mode == "J" :
    new_jam = jam + num
    if new_jam >= 24 :
        new_jam = new_jam % 24
    elif new_jam < 0 :
        new_jam = 24 + new_jam
    jam = new_jam

if mode == "M" :
    new_menit = menit + num
    if new_menit >= 60 :
        new_menit = new_menit % 60
    elif new_menit < 0 :
        new_menit = 60 + new_menit
    menit = new_menit

if mode == "D" :
    new_detik = detik + num
    if new_detik >= 60 :
        new_detik = new_detik % 60
    elif new_detik < 0 :
        new_detik = 60 + new_detik
    detik = new_detik

print(f"Waktu sekarang adalah {jam:02d}:{menit:02d}:{detik:02d}")