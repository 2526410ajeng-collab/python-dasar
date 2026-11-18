class Rekening:
    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah

rek = Rekening("Ajeng", 50000)
rek.setor(10000)
print("Saldo:", rek.get_saldo())
try:
    print(rek.__saldo)
except AttributeError:
    print("Atribut __saldo tidak bisa diakses langsung")
