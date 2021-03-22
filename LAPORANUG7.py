#IMMANUEL JOY PERKASA/71200544

'''Killua sangat senang bermain kata. Beliau meminta kita untuk membuat program yang dapat memainkan suatu kata.
Beliau ingin program dapat berjalan sebagai berikut:
1. Terdapat 2 menu(Angka ke Alphabet dan Membalikan kata)
2. Mengubah angka menjadi alphabet(sesuai dengan urutan alphabet(1=a,26=z))
3. Membalikan urutan kata pada kalimat(aku sayang km. -> km sayang aku.)
4. User dapat memilih program mana yang akan dijalankan.
5. Menu muncul secara terus menerus(looping), baru berhenti ketika inputan user = 0
6. Terkhusus untuk menu 1(angka ke alphabet), hasil akhirnya akan muncul ketika keluar dari menu.
'''
'''
Input
plh= menu plihan user
alfa=' abcdefghijklmnopqrstuvwxyz'
y=''
baru=''
x=urutan alfabet ke-n atau kalimat yang ingin dibalik

proses
if plh==1:
    x=urutan alfabet ke-n
    y+=alfa[x]
elif plh==2:
    x=kalimat yang ingin dibalik
    urut=urutan kata dimulai dari akhir
    baru+=urut

output
Mampu menampilkan hasil kata/kalimat setelah program dijalankan.
'''

alfa=' abcdefghijklmnopqrstuvwxyz'
y=''
while True:
    print()
    print('======= PROGRAM MAIN KATA======')
    print('1. Angka ke Alphabet(1-26)\n2. Membalikan kata pada sebuah kalimat.')
    plh=int(input('Masukkan pilihan anda: '))
    if plh==1:
        x=int(input('Masukkan angka: '))
        if x>0 and x<=26:
            y+=alfa[x]  
        else:
            print('invalid') 
    elif plh==2:
        x=str(input('Masukkan kalimat yang ingin balik: '))
        y=x.strip('.')
        z=y.split(' ')
        baru=''
        for i in range(1,len(z)+1):
            urut=z[len(z)-i]
            baru+=urut+' '
        baru=baru[:-1]
        print(baru+'.')
    elif plh==0:
        if len(y)>0:
            print('Hasil alfaphabetnya adalah',y)
        else:
            print('Tidak ada yang dimasukkan')
        break


