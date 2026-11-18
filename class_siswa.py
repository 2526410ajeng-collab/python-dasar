class Siswa:
    def __init__(self, nama, kota):
        self.nama = nama
        self.kota = kota

    def perkenalan(self):
        print("Nama saya", self.nama, "dari", self.kota)

siswa1 = Siswa("Ajeng", "Subang")
siswa1.perkenalan()
