'''Type hints untuk fungsi'''

# bentuk standar fungsi yang dipelajari

# def fungsi(parameter):
#        hasil = parameter**2
#        print(hasil)

# fungsi(1)
# fungsi("ucup")
# fungsi(True)


def fungsi_dengan_hints(argument:int) -> int:
       '''fungsi dengan type hints'''
       output = 10**argument
       return output

HASIL = fungsi_dengan_hints(3)
print(HASIL)

def display(argument:string):
       print(argument)

display("ucup")


