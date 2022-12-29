nome = input("qual seu nome? ")
idade = int(input("qual sua idade? "))
mensagem = "é menor de idade"
mensagem_else = "é maior de idade"

if idade < 18 :
    print(nome, mensagem, sep="...", end="!")
else :
    print(nome, mensagem_else, sep="!", end="...")    