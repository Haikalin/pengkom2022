tasA = int(input("Masukkan berat tas A: "))
tasB = int(input("Masukkan berat tas B: "))
tasC = int(input("Masukkan berat tas C: "))
batastotal = int(input("Masukkan batasan berat tas keseluruhan: "))
batassalahsatu = int(input("Mauskkan batasan berat tas yang dibawa ke kabin: "))
salah = 0
total = tasA + tasB + tasC

if total > batastotal :
    salah += 1
if tasA <= batassalahsatu or tasB <= batassalahsatu or tasC <= batassalahsatu :
    salah += 0
else :
    salah += 2

if salah == 0 :
    print("Tuan Kil memenuhi peraturan maskapai")
elif salah == 1 :
    print("Tuan Kil melanggar peraturan 1 maskapai")
elif salah == 2 :
    print("Tuan Kil melanggar peraturan 2 maskapai")
else :
    print("Tuan Kil melanggar peraturan 1 dan 2 maskapai")  