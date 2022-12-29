#Métodos da Classe list
#[].append
#Adciona 1 elemento à lista
print(""" 
    [].append
""")
lista = []
lista.append(1)
lista.append("Python")
print(f"A lista está vazia e usando o .append ela ficou assim: {lista}")

#[}.clear
#limpa a lista por completo
print(""" 
    [].clear   
""")
print(lista)
lista.clear()
print(f"Após o .clear a lista ficou assim: {lista}")
lista.append(1)
lista.append("Python")

#[].copy
#copia a lista
print("""
    [].copy
""")
lista.copy()
print(lista)


#[].count
#conta quantas vezes o elemento informado aparece na lista
print("""
    [].count
""")
lista.append(1)
print(lista)
print(f"Quantas vezes temos o elemento '1' da lista é de: {lista.count(1)}")

#[].extend
#adiciona 2 ou mais elementos à lista
print("""
    [].extend
""")
print(lista)
lista.extend(["olá", 15, 30])
print(f"Depois do .extend a lista ficou assim: {lista}")

#[].index
#retorna o índice do elemento informado
print("""
    [].index
""")
print(lista)
print(f"O índice do elemento '15' é: {lista.index(15)}")

#{}.pop
#remove os elementos da listas, removendo o último elemento caso não informamos o índice do elemneto que queremos remover
print("""
    [].pop
""")
print(lista)
print("Vamos usar o .pop informando o índice 1 e usaremos sem informar o índice")
lista.pop(1)
lista.pop()
print(lista)

#[].remove
#remove os elementos da lista, iformando seu valor
print("""
    [].remove
""")
print(lista)
print("vamos usar o .remove informando o valor 'olá'")
lista.remove("olá")
print(lista)

#[].reverse
#espelha a lista
print("""
    [].reverse
""")
print(lista)
lista.reverse()
print(f"A lista espelha usando o .reverse é: {lista}")

#[].sort
#organiza a lista do menor para o maior
#podemos utilizar chaves e o reverse para alterar o método de organização
print("""
    [].sort
""")
lista.extend(["c", "b", "abcd"])
lista.pop(0)
lista.pop(0)
lista.pop(0)
print(lista)
#sem argumentos
lista.sort()
print(f"Organizando em ordem : {lista}")
print("(Com strings, é organizada pela ordem alfabética)")
#reverse = true
lista.sort(reverse = True)
print(f"Organizando, utilizando o reverse, em ordem espelhada: {lista}")
#key len
lista.sort(key = lambda x: len(x))
print(f"Organizando em ordem crescente: {lista}")
#key len, reverse = Ture
lista.sort(key = lambda x: len(x), reverse = True)
print(f"Organizando, utilizando o reverse, em ordem decrescente: {lista}")

#len
#mostra a quantidade de elementos na lista
print("""
    len
""")
print(lista)
print(f"O tamanho da lista é de {len(lista)}")

#sorted
#mesma função do sort, mas necessita de argumentos
print("""
    sorted
""")
print(lista)
print(f"Organizando pelo tamanho: {sorted(lista, key = lambda x: len(x))}")
print(f"Organizando pelo tamanho, mas espelhada (utilizando o reverse): {sorted(lista, key = lambda x: len(x), reverse = True)} ")