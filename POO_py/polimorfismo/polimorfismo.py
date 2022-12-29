#Polimorfismo com herança
class Passaro:
    def voas(self):
        print("voando...")

class Pardal(Passaro):
    def voar(self):
        print("Pardal pode voar")

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")

def plano_voo(obj):
    obj.voar()

plano_voo(Pardal())
plano_voo(Avestruz())
