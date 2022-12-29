LIMITE = 1000
saldo = 5000
saque1 = float(input("qual valor deseja sacar?"))

#if
if saque1 <= LIMITE and saque1 <= saldo :
    print("saque está sendo efetuado")
    saldo -= saque1
    print(f"você tem o saldo de {saldo}")

#if/else
saque2 = float(input("qual valor deseja sacar?"))

if saque2 <= LIMITE and saque2 <= saldo:
    print("saque está sendo efetuado")
    saldo -= saque2
    print(f"você tem o saldo de {saldo}")
else :
    print("Limite excedido")

#if/elif/else
saque3 = float(input("qual valor deseja sacar?"))

if saque3 <= LIMITE and saque3 <= saldo :
    print("saque está sendo efetuado")
    saldo -= saque3
    print(f"você tem o saldo de {saldo}")
elif saque3 > saldo and saldo != 0 and (saque3 <= LIMITE and saldo <= LIMITE):
    print(f"o valor de {saque3} não será afetuado! Efetuando o saque de {saldo}")
    saldo -= saldo
    print(f"você tem o saldo de {saldo}")
else :
    print("Limite excedido")

#if aninhaddo
n = int(input("digite um número"))
NUMERO_LIMITE = 10

if n < 10 :
    if n % 2 == 0 :
        print(f"O numero {n} é menor que {NUMERO_LIMITE} e é par")
    else: 
         print(f"O numero {n} é menor que {NUMERO_LIMITE} e é impar")
else:
    if n % 2 == 0 :
        print(f"O numero {n} é maior que {NUMERO_LIMITE} e é par")
    else:
         print(f"O numero {n} é menor que {NUMERO_LIMITE} e é impar")

#if ternário
saque = float(input("digite um número")) 
SALDO = 750
status = "Falha" if saque <= saldo else "falha"
print(f"{status} ao efetuar o saque")