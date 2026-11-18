harga = {"roti": 4500, "kue": 6000, "donat": 3000}
for nama, nilai in harga.items():
    print(nama, "=", nilai)
for kunci in harga.keys():
    print("Kunci:", kunci)
print("Total:", sum(harga.values()))
