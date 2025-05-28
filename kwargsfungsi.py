'''**kwargs'''

def fungsi(nama,tinggi,berat):
       '''fungsi biasa'''
       print(f"Nama saya {nama} dengan tinggi: {tinggi} dan berat: {berat}")

fungsi("ucup",180,70)

def fungsi(**kwargs):
       '''fungsi dengan kwargs'''
       nama = kwargs["nama"]
       tinggi = kwargs["tinggi"]
       berat = kwargs["berat"]
       print(f"Nama saya {nama} dengan tinggi: {tinggi} dan berat: {berat}")

fungsi(nama="otong",tinggi=170,berat=75)

# studi kasus

def math(*args,**kwargs):
       hasil = 0
       if kwargs["option"] == "tambah":
              for angka in args:
                     hasil += angka
       elif kwargs["option"] == "kali":
              hasil = 1
              for angka in args:
                     hasil *= angka
       else:
              print("option tidak tersedia")

       return hasil
hasil = math(1,2,3,4,option="tambah")
print(f"hasil = {hasil}")
hasil = math(1,2,3,4,option="kali")
print(f"hasil = {hasil}")
