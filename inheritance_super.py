class Hewan:
    def __init__(self, nama):
        self.nama = nama

class Burung(Hewan):
    def __init__(self, nama, bisa_terbang):
        super().__init__(nama)
        self.bisa_terbang = bisa_terbang

kiki = Burung("Kiki", True)
print("Nama:", kiki.nama)
print("Bisa terbang:", kiki.bisa_terbang)
