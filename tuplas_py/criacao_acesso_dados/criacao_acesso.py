#Tuplas
#Criação de tuplas são imutaveis
#entre ()
#podemos criar tuplas apenas colocando os elementos separados por , e entre ()
print("""
    Criação de Tuplas entre ()
""")
frutas = ("laranja", "banana", "pera", "abacaxi", "tomate")
print(frutas)

#tuple
#criar tuplas usando tuple
print("""
    Criação de Tuplas com tuple
""")
letras = tuple("python")
print(letras)

#com números usamos colchetes
numeros = tuple([1, 2, 3, 4])
print(numeros)

#Acesso Direto
#acessamos pelo índice
print("""
    Acesso Direto
""")
print(frutas)
print(frutas[0])
print(frutas[2])

#Índice negativo
print("""
    Índice Negativo
""")
print(f"O elemento com o índice negativo -1 é {frutas[-1]}")

#Tuplas aninhadas
print("""
    Tuplas aninhadas
""")
#são matrizes e para selecionar seus elementos usamos 2 índices sendo de linha e coluna

matriz = (
    (1, 'a', 2),
    ('b', 3, 4),
    (6, 5, 'c',)
)
print(matriz)
print(f'o print da matriz no indice 0 é {matriz[0]} assim pegamos uma linha (uma tupla). Para pegarmos um item devemos informar os indices de linha e coluna, como por exemplo a matriz no indice 1 e 2 é {matriz[1][2]}')

#Fatiamento
print("""
    Fatiasmento
""")
#podemos extrais um conjunto de valores de uma seqyência. Para isso basta passar o indice iniciaç e/ou final para acessar o conjunto. Podemos ainda informar quantas posições o cursor 'dece' pulasno aceso

print(frutas)
print(f'frutas[2:] = {frutas[2:]} frutas[0:3:2] = {frutas[0:3:2]}')

#itraração
print("""
    Iteração
""")
#itrarr usabdo o comando for
print(frutas)
print('usando o comando for para percorrer a tupla frutas')
for fruta in frutas:
    print(fruta)

#Função enumerate
print("""
    emumerate
""")
#dentro do laço for podemos usar a função enumerate
print(frutas)
print('usando a função enumerate dentro do laço for')
for indice, fruta in enumerate(frutas):
    print(f'{indice}: {fruta}')