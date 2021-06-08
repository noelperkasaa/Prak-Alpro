#IMMANUEL JOY PERKASA/71200544
'''
Sekolahmu memberimu tugas untuk membuat kamus yang berisi bahasa buatan kita/user sendiri, namun dengan syarat:
1. Dalam bentuk menu perulangan (5 menu, fungsinya input kata, hapus, lihat, translate, exit)
2. Harus menggunakan regex
'''
'''
INPUT

d = kamus (dict)
kata = tampungan kata untuk fungsi regex
menu = nomor menu inputan user
inp = inputan kata (input/hapus)
cari = cari kata pada kamus (regex)
hapus = hapus kata pada tampungan (kata) (regex)
kalimat = kalimat yang akan di translate user


PROSES

if menu==1:
    program input kata dan arti
elif menu==2:
    program hapus kata dari kamus
elif menu==3:
    program memperlihatkan data dictionary/kamus
elif menu==4:
    program mampu menampilkan hasil translate
elif menu==5:
    exit
else:
    invalid


OUTPUT
Program diharapkan dapat mentranslate kata sesuai isi kamus.
'''
import re
d={}
kata=''

while True:
    print('======PROGRAM KAMUS PRIBADI=======')
    print('1. Input kata & arti\n2. Hapus data\n3. Lihat isi kamus\n4. Translate\n5. Exit')
    menu=int(input('Masukkan nomor menu pilihan anda: '))
    if menu==1:
        jml=int(input('Jumlah kata yang ingin anda input: '))
        for i in range(jml):
            inp=str(input('Masukkan kata: '))
            arti=str(input('Arti dari %s: '%inp))
            d[inp]=arti
            kata+=inp
    elif menu==2:
        print(d)
        inp=str(input('Masukkan kata yang ingin dihapus: '))
        cari=re.findall(inp,kata)
        hapus=re.sub(inp,'',kata)
        if (cari):
            del d[inp]
            kata=hapus
        else:
            print('Kata tidak ditemukan di dalam kamus')
    elif menu==3:
        print('Berikut isi Kamus anda: ')
        print(d)
    elif menu==4:
        kalimat=str(input('Masukkan kalimat yang ingin ditranslate: '))
        spasi=re.split(' ',kalimat)
        for i in spasi:
            if i in d:
                for key,values in d.items():
                    if i==key:
                        print(values,end=' ')
            else:
                print(i,end=' ')
        print()
    elif menu==5:
        print('Anda berhasil keluar')
        break
    else:
        print('Invalid')


        


