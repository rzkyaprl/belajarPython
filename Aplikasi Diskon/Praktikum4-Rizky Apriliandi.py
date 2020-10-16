print("Praktikum IV")
print("------------------------------------------------")
print("Pengujian Diskon")
# TODO membuat input total Bayar
total_bayar=float(input("Total Bayar = "))

# TODO membuat percabangan 
if 100000 > total_bayar :
    print("Bonus : Tidak Mendapat Bonus")
# menggunakan >= karena jika tidak menggunakan 200000 tidak terhitung
elif   200000 >= total_bayar :
    print("Bonus : Kupon Belanja Rp 30.000")
elif total_bayar > 200000 :
    print("Bonus : Kupon Belanja Rp 50.000 + Kartu Anggota")


