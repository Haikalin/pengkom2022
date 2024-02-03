ukuran = int(input("Masukkan nilai m: "))
papan = [['.' for i in range(ukuran)]for j in range(ukuran)]
for i in range(ukuran) :
    for j in range(ukuran) :
        papan[i][j] = input(f"Masukkan elemen matriks ke-{i+1} {j+1}: ")
        if papan[i][j] == "R" :
            barisraja = i
            kolomraja = j

kenakuda = 0
for i in range(ukuran) :
    for j in range(ukuran) :
        if papan[i][j] == 'K' :
            selisihbaris = barisraja-i
            selisihkolom = kolomraja - j
            if selisihbaris == 2 or selisihbaris == -2 :
                if selisihkolom == 1 or selisihkolom == -1 :
                    kenakuda += 1
            elif selisihbaris == 1 or selisihbaris == -1 :
                if selisihkolom == 2 or selisihkolom == -2 :
                    kenakuda += 1

print(kenakuda)