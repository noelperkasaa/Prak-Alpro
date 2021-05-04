#IMMANUEL JOY PERKASA/71200544

'''
Ayahmu yang merupakan pemilik RUMAH MAKAN LEZAT memintamu untuk membuat program untuk membuat menu makanan bagi para pelayan dan
memesan makanan bagi para customer. Apabila kita masuk sebagai pelayan, maka harus memasukkan password terlebih
dahulu sebelum program berjalan. Sementara untuk customer, tidak memerlukan password. Terdapat beberapa syarat untuk
program ini:
1. Semua program berjalan berulang-ulang
2. Menanyakan terlebih dahulu user adalah pelayan atau customer ("exit" untuk keluar dari menu)
3. Program pelayan (Memasukan menu dan harga, menghapus menu, exit)
4. Program customer (Memesan menu, Melihat menu yang sudah dipesan(total pembayaran), memanggil pelayan(exit), exit)
'''
'''
Input
a= Tampungan menu yang dibuat
b= Tampungan menu yang dipesan
total= total pembayaran
code= kata sandi(pelayan)
user= pelayan/customer
password= password pelayan
menu=program yang dipilih user
inp= input menu yang dimasukan ataupun dipesan
harga= harga menu
jml= jumlah pemesanan menu

Proses
if user=='pelayan':
    if password==code:
        menjalankan program untuk pembuatan menu
elif user=='customer':
    menjalan program untuk memesan makanan atau minuman
elif user='exit':
    keluar dari program

Output
mampu menjalan program sesuai dengan user dan menu yang dimasukkan
'''
a=()
b=()
total=0
code='123'
while True:
    user=str(input('Anda pelayan atau customer? ("exit" untuk keluar.)\n'))
    if user=='pelayan':
        password=input('Masukkan password: ')
        if password==code:
            while True:
                print()
                print()
                print('=======RUMAH MAKAN LEZAT========')
                print('1. Memasukan dan Membuat harga menu\n2. Menghapus Menu\n3. Exit')
                menu=int(input('Masukkan nomor menu pilihan anda: '))
                if menu==1:
                    a=dict(a)
                    b=dict(b)
                    inp=str(input('Masukkan menu yang akan dimasukkan: '))
                    harga=int(input('Masukkan harga %s:'%inp))
                    if inp not in a:
                        a[inp]=harga
                        print(a)
                    else:
                        print('Terdapat menu yang sama persis.')
                elif menu==2:
                    inp=str(input('Masukkan menu yang akan dihapus: '))
                    if inp in a:
                        del(a[inp])
                        print(a)
                    else:
                        print('Menu tidak ditemukan')
                elif menu==3:
                    print('Anda telah keluar dari program PELAYAN')
                    print('Berikut adalah menu yang anda buat: ')
                    print(a)
                    break
                else:
                    print('Invalid')
        else:
            print('Password salah')
    elif user=='customer':
        while True:
                print()
                print()
                print('=======RUMAH MAKAN LEZAT========')
                print('1. Lihat dan Pesan Makanan/Minuman\n2. Lihat pesanan anda (Total Pembayaran)\n3. Memanggil pelayan(Tidak self-service)\n4. Exit')
                menu=int(input('Masukkan nomor menu pilihan anda: '))
                if menu==1:
                    print(a)
                    inp=str(input('Masukkan menu makanan/minuman yang akan anda pesan: '))
                    if inp in a:
                        jml=int(input('Berapa yang ingin anda pesan: '))
                        for key,value in a.items():
                            if key==inp:
                                b[key]=value*jml
                                total+=value*jml
                                print(total)
                        print(inp,'berhasil dipesan')
                    else:
                        print('Menu tidak ditemukan')
                elif menu==2:
                    if len(b)>0:
                        print('Berikut adalah menu yang anda pesan')
                        print(b)
                        print('Total pembayarannya adalah',total)
                    else:
                        print('Belum ada menu yang dipesan')
                elif menu==3:
                    print('Silahkan tunggu pelayan untuk melayani pemesanan anda')
                    break
                elif menu==4:
                    print('Anda berhasil keluar')
                    b=tuple(b)
                    print('Pesanan anda:')
                    for i in b:
                        print(i)
                    break
                else:
                    print('Invalid')
    elif user=='exit':
        print('Anda keluar dari program')
        break
    else:
        print('Invalid')
                




                    