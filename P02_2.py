match = int(input("Masukkan jumlah pertandingan: "))
kalahdiB = 0
poin = 0
for i in range(match) :
    pertandingan = i+1
    hasil = input(f"hasil pertandingan ke-{pertandingan}: ")
    if (pertandingan % 2 == 1) or (pertandingan % 2 == 0 and kalahdiB >= 1) :
        if hasil == "W" :
            poin += 3
        elif hasil == "D" :
            poin += 1
    elif pertandingan % 2 == 0 and kalahdiB == 0 :
        if hasil == "L" :
            kalahdiB += 1

print(f"Poin Klub Pengkom saat ini adalah {poin}")
