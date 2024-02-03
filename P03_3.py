size = int(input("Masukkan banyak kota: "))
array = [0 for i in range(size)]

for i in range(size) :
    array[i] = int(input(f"Masukkan perubahan uang di kota {i+1}: "))

uangmax = array[0]
# Kota berupa indeks jadi untuk print indeks + 1
kotaawal = 0
kotaakhir = 0
for i in range(size) :
    for j in range(i, size):
        uang = 0
        kota = i
        for x in range(kota,j+1) :
            uang += array[x]
        if uang > uangmax :
            uangmax = uang
            kotaawal = i+1
            kotaakhir = j+1

print(uangmax,kotaawal,kotaakhir)
            
