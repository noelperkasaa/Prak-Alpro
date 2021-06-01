#IMMANUEL JOY PERKASA/71200544

'''
Pak Budi mempunyai seorang anak yang sedang belajar menghafal bilangan genap, ganjil, dan prima. Sehingga pak Budi
membayarmu untuk membuat program yang dapat mengeluarkan output dengan 3 bilangan di atas, dengan syarat harus menggunakan
fungsi rekursif. Selain 3 bilangan itu, Pak Budi juga ingin kamu membuat bentuk segitiga sesuai dengan tinggi yang
ditentukan oleh anaknya. Program ini harus dalam bentuk Menu.
'''
'''
Input

x= inputan user (int)
menu= nomor menu yang diinginkan user (int)
segitiga(x,y)
prima(x)
genap(x)
ganjil(x)

proses

if menu==1:
    def segitiga(x)
elif menu==2:
    def prima(x)
elif menu==3:
    def ganjil(x)
elif menu==4:
    def genap(x)
elif menu==5:
    break
else:
    invalid

output

mampu menghasilkan output yang sesuai dengan menu yang dipilih user (menggunakan fungsi rekursif)
'''

def segitiga(x,y):
    if x<=0:
        return 0
    else:
        print(' '*y,end='')
        print('*'*(x*2))
        return x*segitiga(x-1,y+1)

def prima(x):
    if x>1:
        if x==2 or x==3 or x==5 or x==7:
            print(x)
            return prima(x-1)
        elif x%2!=0 and x%3!=0 and x%5!=0 and x%7!=0 and x%11!=0: 
            print(x)
            return prima(x-1)
        else:
            return prima(x-1)
def ganjil(x):
    if x>0:
        if x%2==0:
            return ganjil(x-1)
        else:
            print(x)
            return ganjil(x-1)
def genap(x):
    if x>0:
        if x%2==0:
            print(x)
            return genap(x-1)
        else:
            return genap(x-1)

while True:
    print('====PROGRAM BILANGAN DAN SEGITIGA TERBALIK======')
    print('1. Membuat Segitiga Terbalik\n2. Bilangan Prima\n3. Bilangan Ganjil\n4. Bilangan Genap\n5. Exit')
    menu=int(input('Masukkan nomor menu pilihan anda: '))
    if menu==1:
        x=int(input('Masukkan tinggi segitiga: '))
        segitiga(x,1)
    elif menu==2:
        x=int(input('Masukkan range bilangan: '))
        print('Prima: ')
        prima(x)
    elif menu==3:
        x=int(input('Masukkan range bilangan: '))
        print('Ganjil: ')
        ganjil(x)
    elif menu==4:
        x=int(input('Masukkan range bilangan: '))
        print('Genap: ')
        genap(x)
    elif menu==5:
        print('Anda berhasil keluar dari menu')
        break
    else:
        print('Invalid')

