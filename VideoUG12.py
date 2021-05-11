#IMMANUEL JOY PERKASA/71200544

'''
Pecel lele tempat langgananmu mendadak menjadi mewah sekali, sehingga owner dari pecel lele tersebut memintamu untuk 
membuat program self-service. Namun, terdapat beberapa syarat dalam membuat program:
1. Berjalan secara berulang-ulang hingga user ingin exit.
2. Menu dan harga sudah disediakan dari awal dan tidak dapat diubah.
3. Terdapat 3 menu (Pesan, Total bayar, Exit)
4. Menggunakan set.
'''
'''
Input
x=daftar menu
y=tampungan kosong untuk item yang dipesan (list)
bayar=jumlah yang harus dibayar
plh=input menu yang akan dipilih
menu=input item yang akan dipesan/exit
jml=jumlah item yang dipesan

Proses
if menu==1:
    program yang berjalan adalah memesan item
elif menu==2:
    program dapat menunjukan item yang akan dipesan dan total pembayarannya
elif menu==3:
    exit

Output
Mampu menjalan program sesuai dengan menu yang dipilih user.
'''

x={
    'ayam goreng':10000,'ikan goreng':5000,'ayam bakar':12000,'ikan bakar':7000,'bebek goreng':15000,'es teh manis':3000,'es jeruk':3000
    }
y=[]
a=[]
while True:
    print()
    z=set(y)
    print('=======RM PECEL LELE=======')
    print('1. Lihat dan Pesan Menu\n2. Lihat pesanan dan total pembayaran\n3. Exit')
    plh=int(input('Masukkan nomor menu pilihan anda: '))
    if plh==1:
        print(x)
        menu=str(input('Masukkan nama menu/item yang ingin anda pesan: '))
        if menu in x:
            for key,value in x.items():
                if menu==key:
                    jml=int(input('Masukkan jumlah item yang ingin dipesan: '))
                    for i in range(jml):
                        y.append(key)
        else:
            print('Tidak ada menu tersebut')
    elif plh==2:
        bayar=0
        print()
        print('Item\t\tJumlah\t\tTotal')
        for i in z:
            total=0
            n=0
            for j in y:
                if i==j:
                    n+=1
                    for key,value in x.items():
                        if i==key:
                            total+=value
            bayar+=total
            print(i,'\t',n,'\t\t',total)
        print('Total pembayaran untuk pesanan anda adalah Rp.%d'%bayar)
        while True:
            konfir=str(input('Apakah anda sudah yakin untuk pesanan? (Ya/Tidak)'))
            konfir=konfir.lower()
            if konfir=='ya':
                print('Pesanan sudah dikonfirmasi')
                a.append(i)
                break
            elif konfir=='tidak':
                print('Pesanan anda belum dikonfirmasi')
                break
            else:
                print('Invalid')
    
    elif plh==3:
        if len(a)>0:
            print('Tunggu pesanan anda di meja anda.')
            break
        else:
            print('Pesanan tidak jadi untuk dipesan')
            break
    else:
        print('Menu yang anda masukkan salah.')





