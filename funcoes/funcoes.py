#Funções são um bloco de código identificado por um nome e pode receber uma lista de parâmetros, eles podem ou não ter valors padrões.
#usar funções torna o código mais legível e possibilita o reaproveitamento de código, progamando de maneira estruturada
#declarando função
def exibir_mensagem():
    print('Olá Mundo!')
    
def exibir_mensagem1(nome):
    print(f'Seja bem vindo {nome}')
    
def exibir_mensagem2(nome='Neymar jr'):
    print(f'Seja bem vindo {nome}')
    
exibir_mensagem()
exibir_mensagem1(nome='Rodrygo')
exibir_mensagem2()
exibir_mensagem2(nome='Vini jr')

#Retornando valores
#em Py uma função pode retornar mais de um valor usando a palavra return

def calcular_total(numeros):
    return sum(numeros)

def retornar_antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    
    return antecessor, sucessor

print(calcular_total([10, 20, 34]))
print(retornar_antecessor_sucessor(10))

#argumentos nomeados
#funções também pode ser chamadas usando argumentos nomeados da forma cahve=valor

def salvar_carro(marca, modelo, ano, placa):
    print(f'Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}')
    
print(salvar_carro(**{'marca': 'Fiat', 'modelo': 'Palio', 'ano': 1999, 'placa': 'BAC-1234'}))

#ARGS E KWARGS
#Podemos combinar parâmetros obrigatórios com args e kwargs. Quando definidos, o método recebe os valores como tupla para args e dicionário para kwargs

def exibir_poema(data_extenso, *args, **kwargs):
    texto = '\n'.join(args)
    meta_dados = '\n'.join([f'{chave.title()}: {valor}' for chave, valor in kwargs.items()])
    mensagem = f'{data_extenso}\n\n{texto}\n\n{meta_dados}'
    print(mensagem)
    
print(exibir_poema('Zen of Python', 'Beuatiful is better than ugly.', autor='Tim Peters', ano=1999))

#Parâmetros especiais
#para melhor legibilidade e desempenho, faz sentido restringir a maneira pelo qual argumentos possam ser passados
# assim um desenvolvedor precisa apenas olhar para a definição da função para determinar se os itens são passados por
#posição
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
    
print(criar_carro('Palio', 1999, 'abc-1223', marca='Fiat', motor='1.0', combustivel='Gasolina'))

#chave

def criar_carro1(*, modelo, ano, placa):
    print(modelo, ano, placa)
    
print(criar_carro1(modelo='Palio', ano=1999, placa='gtd-5412'))

#posição e chave

def criar_carro2(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
    
print(criar_carro2('Palio', 1999, 'hfd-8437', marca='Fiat', motor='1.0', combustivel='Gasolina'))

#Objetos de primeira classe
#funções também são objetos. Com isso podemos atribuir funções a variáveis, passá-las como parâmetro para funções, usá-las como valores em estruturas de dados
def somar(a, b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f'O resultado da operação {a} + {b} = {resultado}')
    
print(exibir_resultado(10, 10, somar))

#escopo local e global
#dentro do bloco da função o escopo é local. Portanto altreações ali feitas em objetos imutáveis serão eprdidas quando o método terminar de ser executado.
#para usar objetos globais, utilizamos a palava-chave global, que informa que a vairável está sendo manupulada no escopo local é global
salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

print(salario_bonus(500))

#Funções anônimas: Funções Lambda
#Usada mais por um curto período
#Sintaxe: lambda arguments: <expression>
area_quadrado = lambda lado: lado**2

print(area_quadrado(4))

#função map()
#permite percorrermos uma lista, realizando a expressão em cada item
triplo = lambda x: x*3
lista =[4, 5, 6, 7]
print(list(map(triplo, lista)))
