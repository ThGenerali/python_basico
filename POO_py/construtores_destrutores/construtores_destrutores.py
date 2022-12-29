class cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Iniciando a classe")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("removendo instância da classe")

    def latir(self):
        print("Au au")

c = cachorro("Rex", "amarelo")
c.latir()
