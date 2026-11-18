from abc import ABC, abstractmethod

class Hewan(ABC):
    @abstractmethod
    def suara(self):
        pass

class Kucing(Hewan):
    def suara(self):
        return "meong"

mimi = Kucing()
print("Mimi bersuara:", mimi.suara())
try:
    h = Hewan()
except TypeError:
    print("Hewan abstrak tidak bisa dibuat langsung")
