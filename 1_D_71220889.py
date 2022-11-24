print("Ketik 1 untuk menghitung penjumlahan")
print("Ketik 2 untuk menghitung pengurangan")
print("Ketik 3 untuk menghitung perkalian")
print("Ketik 4 untuk menghitung pembagian")
print("Ketik 5 untuk menghitung sisa hasil bagi(modulus")
print("Ketik 6 untuk menghitung pemangkatan")
p = int(input("masukkan pilihan anda: "))
q = int(input("masukkan bilangan pertama: "))
r = int(input("masukkan bilangan kedua: "))
if p == 1 :
    jumlah = q + r
    print("hasil dari",q,"dijumlahkan dengan",r,"adalah",jumlah)
elif p == 2:
    jumlah = q - r
    print("hasil dari",q,"dikurangi dengan",r,"adalah",jumlah)
elif p == 3 :
    jumlah = q * r
    print("hasil dari",q,"dikali dengan",r,"adalah",jumlah)
elif p == 4 :
    jumlah = q/r
    print("hasil dari",q,"dibagi dengan",r,"adalah",jumlah)
elif p == 5 :
    jumlah = q%r
    print("hasil dari",q,"modulo dari",r,"adalah",jumlah)
elif p == 6 :
    jumlah = q**r
    print("hasil dari",q,"pangkat dengan",r,"adalah",jumlah)
    