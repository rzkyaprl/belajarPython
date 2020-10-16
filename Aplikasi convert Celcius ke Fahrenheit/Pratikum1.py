# menampilkan garis 
print("-----------------------------------")

# menampilkan pratikkum I
print("Pratikktum I")

# input untuk var c dan mengubah variable c menjadi tipe data float
c = float(input("Masukan nilai Suhu Celcius = "))

# perhitungan nilai suhu fahrenheit/konversip
f = float(1.8 * c + 32)

# mengconvert float ke string
string_value = str(f)

# mencetak nilai fahrenheit
print("('Suhu Fahrenheit = ', " + string_value + ")")

# menampilkan garis
print("-----------------------------------")
