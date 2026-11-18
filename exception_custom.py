class SaldoTidakCukup(Exception):
    pass

def tarik(saldo, jumlah):
    if jumlah > saldo:
        raise SaldoTidakCukup("Saldo Ajeng tidak cukup")
    return saldo - jumlah

try:
    tarik(50000, 80000)
except SaldoTidakCukup as e:
    print("Error:", e)
