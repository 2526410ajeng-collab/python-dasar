siswa = {"nama": "Ajeng", "kota": "Subang", "sementara": "hapus"}
del siswa["sementara"]
print(siswa)
kota = siswa.pop("kota")
print("Dihapus:", kota)
print(siswa)
