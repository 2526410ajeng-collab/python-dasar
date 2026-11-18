with open("contoh.txt", "w") as f:
    f.write("Roti\n")
    f.write("Kue\n")
    f.write("Donat\n")

with open("contoh.txt", "r") as f:
    for nomor, baris in enumerate(f, start=1):
        print(nomor, baris.strip())
