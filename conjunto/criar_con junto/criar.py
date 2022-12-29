#Cirando sets
print(''''
    Criando sets      
''')

numeros = set([1, 2, 3, 4])
letras = set('abacaxi')
carro = set (('palio', 'celta', 'gol', 'palio'))
print(f'numeros = {numeros} letras = {letras} carro = {carro}')

#Acessando os dados
print(''''
    Acessando os dados      
''')
#Conjuntos em py não suportam indexação e nem fatiamneot, caso queira acessar os seus valores é necessáario onverter para lista

print(letras)
print('transformando em lista')
letras = list(letras)
print(f'letras[0] = {letras[0]}')

#iteração
print(''''
    Iterar sets      
''')
#usa o comando for
for carros in carro:
    print(carros)
    
#enumerate
print(''''
    enumerate      
''')
for indice, numero in numeros:
    print(f'{indice}: {numero}')