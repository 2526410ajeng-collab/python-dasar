def bagi(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Tidak bisa dibagi nol")
    except TypeError:
        print("Tipe data tidak cocok")

print(bagi(10, 2))
bagi(10, 0)
bagi(10, "dua")
