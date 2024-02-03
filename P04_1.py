def factorial (x) :
    hasil = 1
    for i in range(x,0,-1) :
        hasil *= i
    return hasil

def kombinasi(n,k) :
    penyebut = factorial(n)
    pembilang = factorial(n-k)*factorial(k)
    hasil = penyebut // pembilang
    return hasil

n = int(input("Masukkan N: "))
k = int(input("Masukkan K: "))
print(f"Tuan Riz memiliki {kombinasi(n,k)} cara untuk memilih mahasiswa")
    