#IMMANUEL JOY PERKASA/71200544

''' Buatlah program untuk pemesanan/reservasi kamar hotel. Namun program ini berjalan secara terus menerus sebelum user memilih
menu "Exit". Pada program ini terdapat beberapa syarat;
1. Terdapat 4 menu (List kamar kosong, Booking Kamar, Check Out, dan Exit)
2. Terdapat 10 kamar kosong, apabila 10 kamar telah dibooking maka user tidak dapat memesan kamar.
3. Menu Check out berfungsi untuk menandakan bahwa kamar sudah dapat digunakan kembali.
'''
'''
Input
kamar:[1,2,3,4,5,6,7,8,9,10]
menu pilihan user(plh)
nomor pilihan user(nomor)(check out dan reservasi)

proses
plh==1:
print(kamar)
plh==2:
nomor=int(input())
plh==3:
nomor=int(input())
plh==4:
break(program berhenti)

output
berhasil atau tidaknya program berjalan setelah user menjalankan keempat menu.
'''
kamar=[1,2,3,4,5,6,7,8,9,10]

while True:
    print()
    print('======= HOTEL SINAR JAYA =======')
    print('''1. List Kamar Kosong
2. Booking/Reservasi Kamar
3. Check Out
4. Exit''')
    plh=int(input('Masukkan menu pilihan anda: '))
    if plh==1:
        print('Nomor kamar yang tersedia adalah: ',kamar)
    elif plh==2:
        nomor=int(input('Nomor kamar yang ingin anda pesan: '))
        if nomor in kamar:
            kamar.remove(nomor)
            print('Kamar',nomor,'telah berhasil dipesan/booking.')
        elif len(kamar)==0:
            print('Maaf, tidak ada kamar yang tersedia. Datanglah lain kali:)')
            break
        elif nomor not in kamar:
            print('Maaf, nomor kamar anda masukkan sudah dibooking.')
    elif plh==3:
        nomor=int(input('Masukkan nomor kamar anda: '))
        print('Kamar',nomor,'telah Check Out')
        if nomor not in kamar:
            kamar.append(nomor)
        elif nomor in kamar:
            print('Nomor kamar yang anda masukkan salah atau belum check in.')
    elif plh==4:
        print('Terimakasih telah memercayai hotel kami.')
        break
    else:
        print('Invalid, silahkan ulangi lagi')




