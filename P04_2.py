kolom = int(input("Masukkan nilai M: "))
baris = int(input("Masukkan nilai N: "))
barishilang = int(input("Masukkan nilai i: "))
kolomhilang = int(input("Masukkan nilai j: "))
matrix = [[0 for i in range(kolom)]for j in range(baris)]

for i in range(baris) :
    for j in range(kolom) :
        matrix[i][j] = int(input(f"Masukkan elemen baris {i+1} kolom {j+1}: "))

for i in range(baris) :
    for j in range(kolom) :
        if i != barishilang-1 and j != kolomhilang-1 :
            print(matrix[i][j], end=" ")
    if i != barishilang-1 :
        print()