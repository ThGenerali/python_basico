#Criação
#Temos diferentes formas de criarmos as listas
#As listas podem conter todos os tipos de dados

#entre colchetes e separados por vírgula
print("""Criação

 """)
frutas = ["laranja", "maçã", "uva"]
print(frutas)

#Função list
print(""" 

    Função list

""")
letras = list("python")
print(letras)
#a função list acaba listando cada letra como elemento

#função range
print(""" 

    Função range

""")
numeros = list(range(10))
print(numeros)
#a função range vem dentro da list que utilizamos para listar números dentro de um alcance determinado

#Acesso Direto
#selecionamos o elemento desejado da lista pelo seu índice
#o índice começa do 0
print(""" 

    Acesso Direto

""")
print(f"o elemento de índice 0 da lista frutas é {frutas[0]} e o índice 2 é {frutas[2]}")
 
#Índice Negativo
#podemos aceesar os elementos de trás para frente com os índices negativos
#o índice negativo começa por -1
print(""" 

    Índice Negativo

""")
print(f"O último elemento da lista frutas pelo índice -1 é {frutas[-1]} e o primeiro pelo índice -3 {frutas[-3]}")

#Listas Aninhadas
#podemos criar estruturas bidimensionais (tabelas/matrizes)
#para acessarmos os elementos, utilizamos os índices de linha e coluna
print(""" 

    Listas Aninhadas/Matrizes

""")
matriz = [
    frutas,
    numeros,
    letras
]
print(matriz)
print(f"""

O elemento da linha 1 e da coluna 3 é {matriz[0][2]}.
O elemento da lina 2 e coluna 2 é {matriz[1][1]}.
E o elemento da linha 3 e coluna 1, utilizando o índice negativo, é {matriz[-1][-3]} (matriz[-1][-3])

""")

#Fatiamento
#podemos informar uma sequência para extrairmos um conjunto de valores
print(""" 

    Fatiamento

""")
print(numeros)
print(f"""

O conjunto de valores que começa a partir do 3 elemento é {numeros[2:]}.
 O conjunto de valores que termina no terceiro elemento é {numeros[:2]}.
 O conjunto de valores que começa a partir do 2 elemento e termina no 4 elemento é {numeros[1:3]}.
 O conjunto de valores que começa a partir do 2 elemento e termina no 9 elemento de passo 2 é de {numeros[1:8:2]}.
 O conjunto de valores que da a sequência invertida, espelhar, (usando índice negativo) é de {numeros[::-1]}
 
 """)

#Iterar Listas
#podemos percorrer os elementos da lista é utilizando o comando for
print(""" 

    Iterar Listas

""")
print(frutas)
for fruta in frutas:
    print(fruta)
print(numeros)
for numero_impar in numeros[1::2]:
    print(numero_impar)

#Função enumerate
#dentro do laço for, podemos saber qual qual o índice usando a função 
print(""" 

    Função enumerate

""")
print(frutas)
for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")

#Compreensão de listas
#com uma sintaxe curtapara criar uma nova lista com base nos valores de uma lista existente(filtro)
#ou gerar uma nova lista aplicando alguma modificação nos elementos de uma lista existente
print("""

Filtro Versão 1

""")
print(numeros)
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print("""

Filtro Versão 2

""")
print(numeros)
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

print(""" 

Modificando Valores Versão 1

""")
print(numeros)
quadrado = []
for numero in numeros:
    quadrado.append(numero ** 2)
    print(quadrado)

print("""

Modificando Valores Versão 2

""")
print(numeros)
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)