sementara = "akan dihapus"
print("Sebelum hapus:", sementara)
del sementara
try:
    print(sementara)
except NameError:
    print("Variabel sementara sudah dihapus")
