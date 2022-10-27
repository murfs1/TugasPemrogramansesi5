#tugas PD sesi 5 
#1. Buatlah biodata sederhana dengan menggunakan fungsi input(), dan output variabel dengan fungsi format(). 

#deklarasi variabel dan input
#variabel nama
nama=input("masukan nama :")
#variabel kelas
kelas=input("masukan kelas :")
#variabel prodi (program studi)
prodi=input("masukan prodi :")
#variabel umurr
umur=input("masukan umur :")
#variabel hobi
hobi=input("masukan hobi :")

#membuat output dengan fungsi .format()
print("Halo, perkenalkan nama saya {},kelas {},program studi {}. saat ini saya berumur {} tahun dan hobi saya adalah {} ".format(nama,kelas,prodi,umur,hobi))