class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print(self.nama, "sedang makan")

class Kucing(Hewan):
    pass

mimi = Kucing("Mimi")
mimi.makan()
print(isinstance(mimi, Hewan))
