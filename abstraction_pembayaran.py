from abc import ABC, abstractmethod

class Pembayaran(ABC):
    @abstractmethod
    def bayar(self, jumlah):
        pass

class OVO(Pembayaran):
    def bayar(self, jumlah):
        print("Bayar", jumlah, "lewat OVO")

class ShopeePay(Pembayaran):
    def bayar(self, jumlah):
        print("Bayar", jumlah, "lewat ShopeePay")

for metode, jumlah in [(OVO(), 52000), (ShopeePay(), 67000)]:
    metode.bayar(jumlah)
