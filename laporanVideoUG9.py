#71200544/IMMANUEL JOY PERKASA

'''
Dodi, temanmu yang merupakan pemilik Hotel Kusuma memintamu untuk membuat program untuk booking kamar secara self-service.
Dia berharap pelanggan dapat membooking sendiri tanpa kebingungan, namun ada beberapa syarat:
1. Terdapat 7 menu. (Kamar yang tersedia, pesan kamar, check in, check out, kamar yang sudah dipesan, terhubung ke resepsionis, exit)
2. Program berjalan secara terus menerus.
3. Menu 6 dan 7 akan memberhentikan program. (menu 6 karena memanggil resepsionis)
4. Menu akan berulang terus menerus apabila inputan user tidak sesuai.
'''
'''
Input
a=[kamar]
b=[kamar dipesan]
c=[kamar checkin]
plh=pilihan menu yang diinginkan user (int)
kmr=pilihan kamar user (int)
konfir=konfirmasi pemesanan (str(Ya/Tidak))
checkin=check in kamar yang telah dipesan (int)
checkout= checkout kamar yang telah dicheck in (int)

Proses
if plh==1:
    print(kamar yang tersedia)
elif plh==2:
    input(kamar yang ingin dipesan)
    input(konfir(ya/tidak))
elif plh==3:
    memasukkan kamar pesanan ke list kamar dipakai
elif plh==4:
    input(checkout kamar yang telah dipakai)
elif plh==5:
    print(kamar yang telah dipesan)
elif plh==6:
    break
elih plh==7:
    break

output
mampu menampilkan output sesuai dengan menu yang tersedia
'''
a=[100,101,102,103,104,105,106,107,108,109]
b=[]
c=[]
print('======= HOTEL KUSUMA ========')
while True:
    print()
    print('1. Kamar Yang Tersedia\n2. Pesan Kamar\n3. Check In\n4. Check Out\n5. Kamar Yang Sudah dipesan oleh Anda\n6. Memanggil Resepionis(Exit)\n7. Exit')
    print('Gunakan Menu no 6 untuk melakukan pemesanan melalui resepionis')
    plh=int(input('Masukkan nomor menu pilihan anda: '))
    if plh==1:
        if len(a)>0:
            print('Terdapat',len(a),'kamar yang tersedia, yaitu: ')
            print(a)
        else:
            print('Tidak ada kamar yang tersedia.')
    elif plh==2:
        while True:
            kmr=int(input('Masukkan nomor kamar pilihan anda: '))
            if kmr in a:
                konfir=str(input('Apakah anda yakin ingin memesan kamar nomor %d? (Ya/Tidak)'%kmr))
                if konfir=='Ya':
                    b.append(kmr)
                    a.remove(kmr)
                    print('Kamar',kmr,'sudah berhasil dipesan/booking oleh anda')
                    break
                elif konfir=='Tidak':
                    print('Kamar tidak jadi dipesan.')
                    break
            else:
                print('Kamar tidak tersedia.')
    elif plh==3:
        while True:
            checkin=int(input('Masukkan nomor kamar yang sudah anda pesan: '))
            if checkin in b:
                print('Anda berhasil check in')
                c.append(checkin)
                b.remove(checkin)
                break
            elif checkin==0:
                break
            else:
                print('Kamar yang anda check in tidak sesuai dengan pemesanan anda')
    elif plh==4:
        while True:
            checkout=int(input('Masukkan nomor kamar anda: '))
            if checkout in c:
                print('Anda telah check out dari kamar anda')
                c.remove(checkout)
                a.append(checkout)
                break
            elif checkout==0:
                break
            else:
                print('Kamar yang masukkan belum dicheck in.')
    elif plh==5:
        print('Kamar yang sudah anda pesan adalah: ')
        if len(b)>0:
            for i in range (len(b)):
                print('Kamar',b[i])
        else:
            print('Tidak ada kamar yang anda pesan')
    elif plh==6:
        print('Silahkan tunggu resepsionis di Lobby.')
        break
    elif plh==7:
        if len(c)>0:
            print('Selamat datang di Hotel Kusuma. Selamat berisitharat')
            break
        else:
            print('Selamat tinggal, hati-hati di jalan!')
            break
    else:
        print('Menu Invalid')
    

