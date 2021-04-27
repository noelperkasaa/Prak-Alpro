#IMMANUEL JOY PERKASA/71200544
#Sumber soal: https://jagongoding.com/python/latihan-logika/menghitung-huruf-vokal/\
'''
Budi memintamu untuk membuatkan program yang membantu anaknya dalam belajar menghafal dan menghitung huruf vokal dan konsonan.
Selain itu, ia juga meminta untuk membuat konverter huruf ke ASCII, sehingga ia berharap anaknya dapat menghafal ASCII juga.
Namun dalam program tersebut ada beberapa syarat:
1. Program berjalan berulang-ulang hingga user memilih menu exit.
2. Terdapat 5 program (ASCII Converter, Total ASCII, Hitung huruf vokal, Hitung konsonan, Exit)
3. Kalimat yang dimasukkan melalui inputan user.
'''
'''
input
menu=menu pilihan user
total=total penjumlahan bilangan ASCII
vokal=total huruf vokal yang muncul
konsonan=total huruf konsonan yang muncul
inp=inputan kalimat user(str)

proses
if menu==1:
    mengubah huruf menjadi bilangan ASCII
elif menu==2:
    menjumlahkan bilangan ASCII
elif menu==3:
    menghitung huruf vokal
elif menu==4:
    hitung konsonan
elif menu==5:
    exit(break)
else:
    invalid

output
dapat menampilkan output yang sesuai dengan menu menggunakan fungsi dictionary.
'''

while True:
    dic1={}
    total=0
    vokal=0
    konsonan=0
    print()
    print()
    print('==========PROGRAM MAIN HURUF==========')
    print('1. ASCII Converter\n2. Total ASCII\n3. Hitung huruf vokal\n4. Hitung konsonan\n5. Exit')
    menu=int(input('Masukkan nomor menu pilihan anda: '))
    if menu==1:
        inp=str(input('Masukkan kalimat yang anda inginkan: '))
        for i in inp:
            c=ord(i)
            dic1[i]=c
        print(dic1)
    elif menu==2:
        inp=str(input('Masukkan kalimat yang anda inginkan: '))
        for i in inp:
            c=ord(i)
            total+=c
        print('Total bilangan ASCII tersebut adalah',total)
    elif menu==3:
        inp=str(input('Masukkan kalimat yang anda inginkan: '))
        inp=inp.lower()
        for i in inp:
            if i in ['a','i','u','e','o']:
                if i not in dic1:
                    dic1[i]=1
                    vokal+=1
                else:
                    dic1[i]=dic1[i]+1
                    vokal+=1
        if vokal>=1:
            print(dic1)
            print('Jumlah huruf vokal kalimat tersebut adalah:',vokal)
        else:
            print('Tidak ada huruf vokal')
    elif menu==4:
        inp=str(input('Masukkan kalimat yang anda inginkan: '))
        inp=inp.lower()
        for i in inp:
            if i not in ['a','i','u','e','o']:
                if i not in dic1:
                    dic1[i]=1
                    konsonan+=1
                else:
                    dic1[i]=dic1[i]+1
                    konsonan+=1
        if konsonan>=1:
            print(dic1)
            print('Jumlah huruf konsonan kalimat tersebut adalah:',konsonan)
        else:
            print('Tidak ada konsonan')
    elif menu==5:
        print('Anda telah keluar dari program')
        break
    else:
        print('Invalid Input')
    
