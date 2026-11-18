class Hewan:
    def suara(self):
        return "..."

class Kucing(Hewan):
    def suara(self):
        return "meong"

class Burung(Hewan):
    def suara(self):
        return "cuit cuit"

for hewan in [Hewan(), Kucing(), Burung()]:
    print(hewan.suara())
