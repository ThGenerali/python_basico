#for 
texto = input("Informe um texto ")
VOGAIS = "AEIOU"
CONSOANTES = "BCDFGHJKLMNPQRSTVWXYZ"

for letra in texto :
    if letra.upper() in VOGAIS :
        print(f"As vogais de seu texto são: {letra}")
for letra in texto :    
    if letra.upper() in CONSOANTES :
        print(f"As consoantes de seu texto são: {letra}")
#podemos usar else, mas é para deixar o bloco de código mais visível, não é pbrigatório o uso

#range
print(list(range(4)))

#for/range
multiplicador = 0
numero = 1

for numero in range(numero, 11):
    for multiplicador in range(11):
        print(f"{numero} * {multiplicador} = {numero * multiplicador}")
#aqui podemos também usar o else

#while
opcao = -1
saldo = 3500
LIMITE = 1000
extrato = " "

while opcao != 0:
    opcao = int(input("[1] Ver saldo \n[2] Sacar \n[3] Mostrar extrato \n[0] Sair "))
    if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 0:
        if opcao == 1 :
            print(f"Seu saldo é de {saldo}")
        elif opcao == 2 :
            saque = float(input("Qual valor deseja sacar? "))
            if saque <= LIMITE and saque <= saldo :
                print("Efetuando saque...")
                saldo -= saque
                extrato += str(f"{saque} \n")
            else:
                if saque > saldo :
                    print("Saldo excedido")
                if saque > LIMITE :
                    print("Limite excedido")
        elif opcao  == 3:
            print("Exibindo extrato...")
            print(extrato)
    else:
        print("opcção inválida")