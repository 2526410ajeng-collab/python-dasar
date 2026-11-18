try:
    hasil = 10 / 2
except ZeroDivisionError:
    print("Error pembagian")
else:
    print("Berhasil, hasil:", hasil)
finally:
    print("Blok finally selalu jalan")
