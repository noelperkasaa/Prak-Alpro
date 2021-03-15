#IMMANUEL JOY PERKASA/71200544

'''Federasi TaeKwondo ingin membuat program untuk menentukan siapa pemenang suatu pertandingan. Pertandingan tersebut 
ditentukan pemenangnya berdasarkan poin dari juri di setiap rondenya. Namun ada beberapa persyaratan dalam pembuatan 
program tersebut. Berikut Syaratnya:
1. Jumlah juri tidak tertentu pada setiap pertandingannya.
2. Program dapat menginput poin juri pada setiap rondenya.
3. Terdapat 2 petarung
4. Ronde juga tidak tertentu pada setiap pertandingannya (Maks. 12 Ronde)
5. Poin 1-10
'''

'''
Input
a=nama petarung 1
b=nama petarung 2
a1= poin petarung 1
b1= poin petarung 2
ronde= jumlah ronde
juri= jumlah juri
poin1=tambahan poin petarung 1
poin2=tambahan poin petarung 2

proses
if ronde>12 and ronde<1:
    invalid
else:
    for i in range ronde:
        poin1=int(input)
        poin2=int(input)
        a1+=poin1
        b1+=poin2
    
output
Mampu menampilkan total poin pada setiap petarungnya dan mampu menampilkan siapa pemenangnya.
'''

#CODING
a=str(input('Masukkan nama petarung 1: '))
b=str(input('Masukkan nama petarung 2: '))
a1=0
b1=0
ronde=int(input('Masukkan jumlah ronde: '))
juri=int(input('Masukkan jumlah juri: '))

if ronde>12 and ronde<1:
    print('Maaf, inputan anda salah.')
else:
    for i in range(1,ronde+1):
        print()
        print('=======RONDE',i,'=======')
        for j in range(1,juri+1):
            print('Juri',j)
            poin1=int(input('Masukkan poin petarung 1: '))
            a1+=poin1
            poin2=int(input('Masukkan poin petarung 2: '))
            b1+=poin2
        print(a,':',a1)
        print(b,':',b1)
    if a1>b1:
        print('Pemenangnya adalah',a)
    elif b1>a1:
        print('Pemenangnya adalah',b)
    else:
        print('Pertandingan imbang.')


        












        


