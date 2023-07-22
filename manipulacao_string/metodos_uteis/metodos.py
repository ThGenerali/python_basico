from platform import python_implementation


demonstracao = "pYThOn"

#maiúscola
print(demonstracao.upper())
#transforma todas caracteres em maiúsculo

#minúsculo
print(demonstracao.lower())
#transforma todas caracteres em minúsculo

#título
print(demonstracao.title())
#transfomra em formato de título (primeira letra maiúscula e as outras minúscula)

demonstracao = "     Python  "

#eliminando todo espaço em branco 
print(demonstracao.strip())

#eliminando o espaço em branco da esquerda
print(demonstracao.lstrip())

#eliminando o espaço em branco da direita
print(demonstracao.rstrip())

demonstracao = "python"

#centralização
print(demonstracao.center(10 , "$"))
#centraliza a variável. primeiro argumento é a quantidade de caracteres que irá ocupar e o segundo argumento é opcional, mas irá prencher o espaço restante para bater a quantidade com o caractere selecionado

#junção
print(".".join(demonstracao))
#irá adicionar o caractere selecionado entre os caracteres da variável

#concatenação - Une duas ou mais strings em uma única
#string1 + string2
pa = 'conca'
la = 'tena'
vra = 'ção'
palavra = pa + la + vra
print(f'string1: {pa}. string2: {la}. string3: {vra}. Soma das strings: {palavra}')

#repetição - Repete o valor da string n vezes
#string * num. repetições
repeticao = 3
while repeticao != 0:
  print(f'{repeticao} repetições: {(palavra + ". ") * repeticao}')
  repeticao -= 1
  
#filiação - Verifica se uma string existe dentro de outra
#string1 in string2
print(f'String1: {pa}. String2: {palavra}. Verificação da string1 na string2: {pa in palavra}')
print(f'String1: {pa}. String2: {la}. Verificação da string1 na string2: {pa in la}')

#não filiação - Verifica se uma string não existe dentro da outra
#string1 not in string 2
print(f'String1: {pa}. String2: {palavra}. Verificação da string1 na string2: {pa not in palavra}')
print(f'String1: {pa}. String2: {vra}. Verificação da string1 na string2: {pa not in vra}')

#replace - substitui uma string por outra
#string.replace(string substituida, string pra substituir)
print(f'palavra: {palavra}. Substituição das strings: {palavra.replace(pa, la)}')

#startswith - Verifica se a string começa com o valor de outra string
#string1.startswith(string2)
print(f'Verificando se {palavra} começa com {pa}: {palavra.startswith(pa)}')

#endswith - Verifica se a string termina com o valor de outra string
#string1.endswith(string2)
print(f'Verificando se {palavra} termina com {vra}: {palavra.endswith(vra)}')

#find - retorna o índice da primeira letra da palavra de uma string em outra string (a função index tem mesmo objetivo, mas caso não encontrado da erro)
#string1.find(string2)
print(f'Procurando {la} em {palavra}. Índice: {palavra.find(la)}')

#rfind - retorna o índice da última letra da palavra de uma string em outra string (a função rindex tem mesmo objetivo, mas caso não encontrado da erro)
#string1.rfind(string2)
print(f'Procurando {la} em {palavra}. Índice: {palavra.rfind(la)}')

#split - Divide a string em outras strings que são separadas por um valor específico
#string.split(valor)
palavra = pa + '. ' + la + '; ' + vra
print(f'Divisão de {palavra} por espaço: {palavra.split()}')
print(f'Divisão de {palavra} por ponto e vírgula: {palavra.split(";")}')

#ljust - Retorna um string justificado à esquerda em um campo de tamanho largura
#string.ljust(largura)
print(f'Ajustando pra esquerda de {palavra} com 11 de largura: a {palavra.ljust(11)} a')

#rjust - Retorna um string justificado à direita em um campo de tamanho largura
#string.rjust(largura)
print(f'Ajustando pra direita de {palavra} com 11 de largura: a {palavra.rjust(11)} a')

#ord - traz o valor ordinal de cada letra (letras minúsculas e maiúsculas tem valores diferentes)
#ord(letra)
for letra in palavra:
  print(f'Valor ordinal de {letra}: {ord(letra)}')
  
#chr - traz a letra equivalente ao valor ordinal
#chr(valor ordinal)
for letra in palavra:
  print(f'Caractere do valor ordinal {ord(letra)}: {chr(ord(letra))}')
  
#O string string.ascii_lowercase contém todas as letras ASCII que o sistema considera seremminúsculas.
#Da mesma forma, string.ascii_uppercase contém todas as letras maiúsculas.
#string.punctuation contém todos os caracteres considerados símbolos de pontuação.



  