size = int(input("Masukkan nilai banyak data: "))
array = [0 for i in range(size)]
for i in range(size) :
    array[i] = int(input(f"Masukkan data ke-{i+1}: "))
find = int(input("Masukkan nilai yang dicari: "))
N = int(input("Masukkan nilai N: "))
count  = 0
for i in range(size) :
    if array[i] == find :
        count += 1
        if count == N :
            print(f"Nilai {find} ke-{N} berada pada indeks {i}")