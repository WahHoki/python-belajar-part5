## global dan local scope

nama_global = 'Andi' # <- variabel global

# akses variabel global dalam fungsi
def fungsi1():
       print(f"Nama dalam fungsi {nama_global}")

fungsi1()

# akses variabel global dalam loop
for i in range(0,5):
       print(f"loop {i} - {nama_global}")

# percabangan
if True:
       print(f"Nama dalam percabangan {nama_global}")

# variabel lokal scope
def fungsi2():
       nama_local = 'Budi' # <- variabel lokal

fungsi2()
# print(nama_local) # <- error, nama_local tidak dikenal

# contoh penggunaan
def say_budi():
       print(f"Halo {nama}")

nama = "Budi"
say_budi()

# contoh 2: merubah variabel global
angka = 0
nama = "ucup"

def ubah(nilai_baru, nama_baru):
       global angka 
       global nama
       angka = nilai_baru
       nama = nama_baru
print(angka,nama) # <- 0
ubah(5,"budi")
print(angka, nama) # <- 0

# contoh 3
angka = 0

for i in range (0,5):
       angka += i
       angka_dummy = 0

print(angka)
print(angka_dummy)


if True:
       angka = 5
       angka_dummy = 10

print(angka)
print(angka_dummy)
