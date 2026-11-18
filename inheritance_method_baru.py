class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print(self.nama, "sedang makan")

class Anjing(Hewan):
    def menggonggong(self):
        print(self.nama, "menggonggong: guk guk")

bobi = Anjing("Bobi")
bobi.makan()
bobi.menggonggong()
