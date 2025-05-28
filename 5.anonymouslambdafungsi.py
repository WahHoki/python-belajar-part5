# fungsi lambda

def kuadrat(angka):
       return angka**2

print(f"Hasil kuadrat dari 5 adalah {kuadrat(5)}")

# kita coba dengan lambda
# output = lambda argument : expression
kuadrat = lambda angka:angka**2
print(f"Hasil lambda kuadrat dari 5 adalah {kuadrat(5)}")

pangkat = lambda num,pow : num**pow
print(f"Hasil pangkat dari 2 pangkat 3 adalah {pangkat(2,3)}")

# sorting untuk list
data_list = ["apel","jeruk","mangga","pisang","durian"]
data_list.sort()
print(f"Data list setelah di sort {data_list}")

#sorting pakai panjang
def panjang_nama(nama):
    return len(nama)

data_list.sort(key=panjang_nama)
print(f"Data list setelah di sort berdasarkan panjang {data_list}")

# sort pakai lambda
data_list = ["apel","jeruk","mangga","pisang","durian"]
data_list.sort(key=lambda nama:len(nama))
print(f"Data list setelah di sort berdasarkan panjang {data_list}")

# filter
data_angka = [1,2,3,4,5,6,7,8,9,10]

def kurang_dari_lima(angka):
       return angka < 5

data_angka_baru = list(filter(kurang_dari_lima,data_angka))
data_angka_baru = list(filter(lambda x:x<7,data_angka))
print((data_angka_baru))

# filter angka genap
data_genap = list(filter(lambda x:x%2==0,data_angka))
print(data_genap)

# filter angka ganjil
data_ganjil = list(filter(lambda x:x%2!=0,data_angka))
print(data_ganjil)

# kelipatan 3
data_3 = list(filter(lambda x:x%3==0,data_angka))
print(data_3)

# annonymous function
# currying <- haskel lambda

def pangkat(angka,n):
       hasil = angka**n
       return hasil

data_hasil = pangkat(2,3)

print(f"fungsi biasa {data_hasil}")

# dengan currying menjadi
def pangkat(angka):
       return lambda n:angka**n

pangkat2 = pangkat(2)
print(f"fungsi lambda {pangkat2(5)}")
pangkat3 = pangkat(3)
print(f"fungsi lambda {pangkat3(5)}")
print(f"fungsi lambda {pangkat(4)(5)}")
