# latihan fungsi
 
import os

# program menghitung luas dan keliling persegi panjang

# membuat header program
# os.system("cls")

# print(f"{'program menghitung luas':^40}")
# print(f"{'dan keliling persegi panjang':^40}")
# print("="*40)

# # mengambil input user
# LEBAR = int(input("Masukkan lebar: "))
# PANJANG = int(input("Masukkan panjang: "))

# # program menghitung luas
# LUAS = LEBAR * PANJANG
# KELILING = 2 * (LEBAR + PANJANG)

# # TAMPILKAN HASILNYA
# print(f"Luas persegi panjang adalah: {LUAS}")
# print(f"Keliling persegi panjang adalah: {KELILING}")

def header():
       '''Fungsi untuk menampilkan header program'''
       os.system("cls")
       print(f"{'program menghitung luas':^40}")
       print(f"{'dan keliling persegi panjang':^40}")
       print("="*40)

def input_user():
       '''Fungsi untuk mengambil input dari user'''
       lebar = int(input("Masukkan lebar: "))
       panjang = int(input("Masukkan panjang: "))

       return lebar, panjang

def hitung_luas(lebar, panjang):
       '''Fungsi untuk menghitung luas persegi panjang'''
       luas = lebar * panjang
       return luas

def hitung_keliling(lebar, panjang):
       '''Fungsi untuk menghitung keliling persegi panjang'''
       keliling = 2 * (lebar + panjang)
       return keliling

def display(message,value):
       '''fungsi display'''
       print(f"hasil perhitungan {message} = {value}")


while True:
       header()
       LEBAR,PANJANG = input_user()
       LUAS = hitung_luas(LEBAR,PANJANG)
       KELILING = hitung_keliling(LEBAR,PANJANG)

       display("luas",LUAS)
       display("keliling",KELILING)

       isContinue = input("Apakah anda ingin melanjutkan (y/n)? ")
       if isContinue == "n":
              break

print("Terima kasih telah menggunakan program ini")
