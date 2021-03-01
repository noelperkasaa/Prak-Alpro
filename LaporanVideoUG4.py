#IMMANUEL JOY PERKASA/71200544


'''
REFERENSI:
https://www.pythonindo.com/menentukan-semua-bilangan-prima-pada-rentang-tertentu/

Buatlah sebuah program dengan fungsi sebagai berikut:
1. Mampu mencari bilangan prima dengan range yang sudah ditentukan oleh inputan user.
2. Mampu mencari bilangan yang habis dibagi oleh bilangan pembaginya. Bilangan pembaginya(z) dan rangenya ditentukan oleh 
   inputan user. (modulus=0)
3. Mampu menampilkan berapa jumlah anggota bilangan yang masuk ke dalam list.
4. Dengan ketentuan, setiap fungsinya hanya mampu menghitung satu fitur. (Bilangan Prima atau Modulus)
'''
'''
input:
def prima(x,y)
def modulo(x,y)
plh = untuk memilih program yang akan dijalan (1 atau 2)
1. bilangan prima
2. modulus

x = range awal(input user)
y = range akhir(input user)
z = bilangan pembagi (modulus)

proses:
if plh==1:
    maka program yang akan berjalan adalah prima(x,y)
if plh==2:
    maka program yang akan berjalan adalah modulo(x,y)

output:
Mampu menampilkan bilangan prima atau bilangan yang habis dibagi oleh z, beserta dengan jumlah anggota pada list nya
'''
def prima(x,y):
    a=[]
    for i in range(x,y+1):
        if i>1:
            for j in range(2,i):
                if (i%j)==0:
                    break
            else:
                a.append(i)
        else: 
            pass
    return a
def modulo(x,y):
    a=[]
    for i in range(x,y+1):
        if i%z==0:
            a.append(i)
    else:
        pass
    return a

print('====SELAMAT DATANG====')
print('1. Bilangan Prima.\n2. Bilangan yang habis dibagi oleh n')
plh=int(input('Pilih fungsi yang anda inginkan: '))
if plh==1:
    x=int(input('Masukkan range awal:'))
    y=int(input('Masukkan range akhir:'))
    print(prima(x,y))
    print('Terdapat',len(prima(x,y)),'bilangan prima dari range',x,'hingga',y)
elif plh==2:
    x=int(input('Masukkan range awal:'))
    y=int(input('Masukkan range akhir:'))
    z=int(input('Bilangan pembagi: '))
    print(modulo(x,y))
    print('Terdapat',len(modulo(x,y)),'bilangan modulus = 0 dari range',x,'hingga',y,'dengan hasil pembagi',z)



