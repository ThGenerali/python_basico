#Herança simples
class Veiculo:
    def __init__(self, cor, placa, nmr_rodas):
        self.cor = cor
        self.placa = placa
        self.nmr_rodas = nmr_rodas
    
    def ligar_motor(self):
        print("Ligando motor")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}" 

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, nmr_rodas, carregado):
        super().__init__(cor, placa, nmr_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

moto = Motocicleta("amarela", "cba-4321", 2)
carro = Carro("preto", "abc-1234", 4)
caminhao = Caminhao("azul", "acb-1324", 8, False)
print(moto)
print(carro)
print(caminhao)
caminhao.esta_carregado()

#Herança composta
class Animal:
    def __init__(self, nmr_patas):
        self.nmr_patas = nmr_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

class Gato(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, nmr_patas):
        print(Ornitorrinco.mro())
        super().__init__(cor_bico=cor_bico, cor_pelo=cor_pelo, nmr_patas=nmr_patas)

gato = Gato(nmr_patas=4, cor_pelo="preto")
print(gato)

ornitorrinco = Ornitorrinco(nmr_patas=4, cor_pelo="vermelho", cor_bico="laranja")
print(ornitorrinco)