#IMMANUEL JOY PERKASA/71200544

'''
Pak Budi yang merupakan guru Matematika memintamu untuk membuat program yang mampu menginput nilai
setiap murid. Tentu saja terdapat beberapa syarat, berikut syaratnya:
1. Terdapat 4 Menu (Input nilai, Rata-rata, Pengelompokan(A-F), Lihat Data) 
2. Program berjalan terus menerus dan keluar ketika menginput angka menu diluar program.
3. Pengelompokannya adalah (F<=40,E<=50,D<=60,C=<70,B<=80,A<=100)
4. Output harus dalam bentuk text document (.txt), karena Pak Budi ingin membukanya outputnya lebih mudah 
tanpa harus membuka program ini.
'''
'''
Input
plh=pilihan menu user(1-4)
siswa=jumlah siswa yang ingin diinputkan
nama=nama siswa
nilai=nilai siswa

proses
if plh==1:
    program akan memasukkan data nama dan nilai siswa
elif plh==2:
    program akan menghitung rata
elif plh==3:
    program akan melakukan pengelompokan data(A= total siswa yang mendapat nilai A)
elif plh==4:
    mampu memunculkan data diprogram
else:
    keluar

output
mampu menunjukan data nilai dan nama siswa di text document(notepad)
'''
handle=open('nilai.txt','w')
handle.close()
a=0
b=0
c=0
d=0
e=0
f=0
total=0
print('=====NILAI SISWA======')
while True:
    print()
    print('1. Input Data\n2. Rata-rata\n3. Pengelompokan nilai\n4. Lihat Data')
    try:
        plh=int(input('Masukkan nomor menu pilihan anda: '))
    except:
        print('Menu tidak diketahui')
    else:
        if plh==1:
            a=int(a)
            b=int(b)
            c=int(c)
            d=int(d)
            e=int(e)
            f=int(f)
            siswa=int(input('Masukkan jumlah siswa: '))
            for i in range(1,siswa+1):
                handle=open('nilai.txt','a')
                print('=====SISWA %d======'%i)
                nama=str(input('Masukkan nama siswa: '))
                nilai=int(input('Nilai siswa: '))
                total+=nilai
                if nilai<=40:
                    nilai=str(nilai)
                    handle.write(nama+': '+nilai+'(F)\n')
                    f+=1
                elif nilai<=50:
                    nilai=str(nilai)
                    handle.write(nama+': '+nilai+'(E)\n')
                    e+=1
                elif nilai<=60:
                    nilai=str(nilai)
                    handle.write(nama+': '+nilai+'(D)\n')
                    d+=1
                elif nilai<=70:
                    nilai=str(nilai)
                    handle.write(nama+': '+nilai+'(C)\n')
                    c+=1
                elif nilai<=80:
                    nilai=str(nilai)
                    handle.write(nama+': '+nilai+'(B)\n')
                    b+=1
                elif nilai<=100:
                    nilai=str(nilai)
                    handle.write(nama+': '+nilai+'(A)\n')
                    a+=1
                else:
                    print('Invalid')
                handle.close()
        elif plh==2:
            rata=total/siswa
            rata=str(rata)
            handle=open('nilai.txt','a')
            handle.write('Rata-rata: '+rata+'\n')
            handle.close()
        elif plh==3:
            if a>0 or b>0 or c>0 or d>0 or e>0 or f>0:
                a=str(a)
                b=str(b)
                c=str(c)
                d=str(d)
                e=str(e)
                f=str(f)
                handle=open('nilai.txt','a')
                handle.write('A:'+a+'\n')
                handle.write('B:'+b+'\n')
                handle.write('C:'+c+'\n')
                handle.write('D:'+d+'\n')
                handle.write('E:'+e+'\n')
                handle.write('F:'+f+'\n')
                handle.close()
            else:
                print('Belum ada nilai yang masuk')
        elif plh==4:
            handle=open('nilai.txt','r')
            print(handle.read())
            handle.close()
        else:
            break


                    



    
        





