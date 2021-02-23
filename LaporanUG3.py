#IMMANUEL JOY PERKASA/71200544

'''
Mari kita membuat game dari dua buah dek kartu yang masing-masing memiliki nilai 1-30. Game ini membutuhkan dua kartu yang diberikan
secara acak dan salah satunya akan diberikan ke player/user. Untuk memenang permainan ini pemain/user membutuhkan 20 poin.
Untuk mendapatkan poin, player/user harus menebak nilai kartu yang mereka dapatkan lebih tinggi atau lebih rendah dari kartu satunya. 
Berikut adalah peraturan dan ketentuan game ini:
a.) Apabila player dapat nilai kartu dengan benar, maka akan mendapatkan 10 poin. .
b.) Apabila  player menebak nilai kartunya dengan salah maka permainan akan selesai.
c.) Game ini hanya dapat dimainkan oleh orang yang sudah berusia 18 tahun ke atas.
d.) Gunakan 'high' untuk menebak nilai kartu player lebih tinggi dari kartu satunya dan gunakan 'low'  untuk menebak nilai
    kartu player lebih rendah dari kartu satunya.
'''
'''
input:
nama= nama user/pemain
umur=umur pemain (harus 18 tahun ke atas)
high/low
x=kartu user
y=kartu musuh

proses
x>y harus high(menang)
x<y harus low(menang)

output
menang= selamat anda memenangkan permainan ini(20 poin)
kalah= permainan selesai.
'''
import random
print('====SELAMAT DATANG==== .\n Peringatan: Game ini hanya boleh dimainkan oleh orang umur 18 tahun ke atas')
nama=str(input('Masukkan nama pemain: '))
umur=int(input('Masukkan umur anda: '))

poin=0

if umur>=18:
    print('Umur anda mencukupi untuk syarat permainan .\n Selamat bermain!')
    print()
    x=random.randint(1,30)
    y=random.randint(1,30)
    print('Berikut adalah kartu anda:',x)
    a=str(input('High/Low:'))
    f=a.lower()
    print('Berikut adalah kartu musuh:',y)
    if x>y:
        if f=='high':
            print('Selamat tebakan anda benar!')
            poin1=poin+10
            print('Poin anda sekarang adalah ',poin1)
            print()
            x=random.randint(1,30)
            y=random.randint(1,30)
            print('Berikut adalah kartu anda:',x)
            a=str(input('High/Low:'))
            f=a.lower()
            print('Berikut adalah kartu musuh:',y)
            if f=='high':
                print('Selamat tebakan anda benar!')
                poin2=poin1+10
                print('Poin anda sekarang adalah ',poin2)
                if poin2==20:
                    print('Selamat',nama,'!!! Anda memenangkan permainan ini!!')
            elif f=='low':
                print('Maaf tebakan anda salah')
        elif f=='low':
            print('Maaf tebakan anda salah')
    elif x<y:
        if f=='low':
            print('Selamat tebakan anda benar!')
            poin1=poin+10
            print('Poin anda sekarang adalah ',poin1)
            print()
            x=random.randint(1,30)
            y=random.randint(1,30)
            print('Berikut adalah kartu anda:',x)
            a=str(input('High/Low:'))
            f=a.lower()
            print('Berikut adalah kartu musuh:',y)
            if f=='low':
                print('Selamat tebakan anda benar!')
                poin2=poin1+10
                print('Poin anda sekarang adalah ',poin2)
                if poin2==20:
                    print('Selamat',nama,'!!! Anda memenangkan permainan ini!!')
            elif f=='high':
                print('Maaf tebakan anda salah')
        elif f=='high':
            print('Maaf tebakan anda salah')
    else:
        print('Invalid')
else:
    print('Maaf umur anda belum mencukupi.')
    
                
            


                
                  
               

                    


                                    


                        
                        
        






