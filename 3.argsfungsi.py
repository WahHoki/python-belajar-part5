'''*args'''

def fungsi(nama,tinggi,berat):
       print(f"Nama saya {nama} dengan tinggi: {tinggi} dan berat: {berat}")

fungsi("ucup",170,70)

def fungsi(data_list):
       data = data_list.copy()
       nama = data[0]
       tinggi = data[1]
       berat = data[2]
       print(f"Nama saya {nama} dengan tinggi: {tinggi} dan berat: {berat}")

fungsi(["otong",180,75])

# kenalan dengan *args

def fungsi(*args):
       nama = args[0]
       tinggi = args[1]
       berat = args[2]
       print(f"Nama saya {nama} dengan tinggi: {tinggi} dan berat: {berat}")

fungsi("ucup",170,70)

# studi kasus

def tambah(*data):
       output = 0
       for angka in data:
              output += angka

       return output

hasil = tambah(1,2,3,4,5)
print(f"hasil = {hasil}")

hasil = tambah(10,5,11,43)
print(f"hasil = {hasil}")


def kurang(*data):
       output = 100
       for angka in data:
              output -= angka

       return output

hasil = kurang(36,12,5)
print(f"hasil = {hasil}")
