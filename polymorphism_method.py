class Kucing:
    def suara(self):
        return "meong"

class Anjing:
    def suara(self):
        return "guk guk"

for hewan in [Kucing(), Anjing()]:
    print(hewan.suara())
