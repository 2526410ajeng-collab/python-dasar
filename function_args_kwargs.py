def jumlahkan(*angka):
    return sum(angka)

def profil(**data):
    for kunci, isi in data.items():
        print(kunci, "=", isi)

print("Jumlah:", jumlahkan(1, 2, 3, 4))
profil(nama="Ajeng", kota="Subang")
