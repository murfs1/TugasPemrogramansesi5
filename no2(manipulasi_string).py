#tugas PD sesi 5 
#Jika terdapat kalimat UNIVERSITAS NUSA PUTRA SUKABUMI buatlah kode
#program untuk menampilkan output:
#a. putra nusa
#b. NIVERSITAS NSA PTRA SKABMI
#C. SUKABUMI PUTRA NUSA UNIVERSITAS
#d. UNPS
#e. TAS SAPU BUMI

#deklarasi varibel
kalimat = "UNIVERSITAS NUSA PUTRA SUKABUMI"

#membuat output point a dengan mengambil index dan membuanya menjadi huruf kecil 
print("point a :",kalimat[17:22].lower(),kalimat[12:16].lower()) #output : putra nusa
#membuat output point b 
print("point b :",kalimat[1:11],kalimat[12]+kalimat[14:16],kalimat[17]+kalimat[19:22],kalimat[23]+kalimat[25:28]+kalimat[29:31]) #output : NIVERSITAS NSA PTRA SKABMI
#membuat output point c 
print("point c :",kalimat[22:31],kalimat[17:22],kalimat[12:16],kalimat[0:11]) #output : SUKABUMI PUTRA NUSA UNIVERSITAS
#membuat output point d
print("point d :",kalimat[0]+kalimat[12]+kalimat[17]+kalimat[23]) #output : UNPS 
#membuat output point e
print("point e :",kalimat[8:11],kalimat[14:16]+kalimat[17:19],kalimat[27:31]) #output : TAS SAPU BUMI
