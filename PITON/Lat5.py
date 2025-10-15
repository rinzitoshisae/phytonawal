# Minta input dari pengguna
usia = int(input("Masukkan usia kamu: "))

# Percabangan untuk menentukan kategori usia
if usia >= 0 and usia <= 13:
    print("sek anak anak mas samean g oleh ndelok ***** sek an")
elif usia >= 14 and usia <= 24:
    print("sek remaja mas awakmu sek iso menikmati orep lah intie")
elif usia >= 25 and usia <= 49:
    print("Dewasa mas samean wes gduk arek cilik neh")
elif usia >= 50:
    print("Wes Tuek/Lansia Pean Wes Karek Matie Tok ")
else:
    print("Usia tidak valid")