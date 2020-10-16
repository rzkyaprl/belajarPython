# Pratikkum III
print("Praktikum III")

print("1. Bilangan 4/9 dan 5/8")
# cek menggunakan operand >
print("Apakah 4/9 lebih besar dari 5/8?", 4/9 > 5/8)
# cek menggunakan operand <
print("Apakah 4/9 lebih kecil dari 5/8?", 4/9 < 5/8)

print("------------------------------------------------")
print("2. Bilangan 7/3 dan 24/7")
# cek menggunakan operand >
print("Apakah 7/3 lebih besar dari 24/7?", 7/3 > 24/7)
# cek menggunakan operand >
print("Apakah 7/3 lebih kecil dari 24/7?", 7/3 < 24/7)
print("------------------------------------------------")
print("3. Perhitungan (75000+25%+50%)dan(75000+75%)")
# TODO membuat hasil perhitungan disko
harga = 75000
hasil_test = harga * (25/100)
hasil_pertama = hasil_test * (50/100) + harga
hasil_kedua = harga * (75/100) + harga
# TODO cek apakah hasil pertama memiliki nilai sesuai
print("Apakah hasil (75000+25%+50%) sama dengan hasil (75000+75%)?", hasil_pertama == hasil_kedua)
# TODO Cetak hasil pertama
print("75000+25%+50% = ", hasil_pertama)
# TODO Cetak Hasil kedua
print("75000+75%     = ", hasil_kedua)
