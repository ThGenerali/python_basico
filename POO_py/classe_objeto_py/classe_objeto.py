#Classe
print('''
    Classe  
    ''')
class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def latir(self):
        print('auau')
        
    def dormir(self):
        self.acordado = False
        print('ZZZZZzZzZzZzzzzz...')
    
print(Cachorro)
        
#Objeto
print('''
    Objeto
    ''')

cao_1 = Cachorro('chappie', 'amarelo', False)
cao_2 = Cachorro('aladin', 'branco e preto')
print(cao_1)
print(cao_2)
cao_1.latir()

print(cao_2.acordado)
cao_2.dormir()
print(cao_2.acordado)
