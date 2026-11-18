class BankAccount:
    def __init__(self, pemilik, saldo=0):
        self.pemilik = pemilik
        self.saldo = saldo

    def setor(self, jumlah):
        self.saldo += jumlah

    def tarik(self, jumlah):
        if jumlah > self.saldo:
            print("Saldo tidak cukup")
        else:
            self.saldo -= jumlah

akun = BankAccount("Ajeng", 50000)
akun.setor(25000)
print("Saldo:", akun.saldo)
akun.tarik(100000)
akun.tarik(30000)
print("Saldo akhir:", akun.saldo)
