f = open("data.txt", "r")
for baris in f:
    print("Baris:", baris.strip())
f.close()
