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