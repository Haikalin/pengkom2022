size = int(input("Masukkan banyak data: "))
N = int(input("Masukan nilai N: "))
array = [0 for i in range(size)]
for i in range(size) :
    array[i] = int(input(f"Masukkan data ke-{i+1}: "))

for i in range(size) :
    for j in range(i+1,size) :
        if array[i] < array[j] :
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

print(f'Nilai terbesar ke-{N} adalah {array[N-1]}')