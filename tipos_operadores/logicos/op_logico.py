saldo = 750
saque = 200
limite = 1000

#operador E
print_resultado = saldo >= saque and saque <= limite
#todos valores têm de ser verdadeiro para o operador E ser verdadeiro
print(print_resultado)

#operador OU
print_resultado = saldo >= saque or saque >= limite
#precisa de apenas 1 valor ser verdadeirp para o operador OU ser verdadeiro
print(print_resultado)

#operador NOT
print_resultado = not saldo
#inverte o valor booleano da variável
print(print_resultado)
saldo = 0
print_resultado = not saldo
print(print_resultado)

#parentêses
saldo = 750
print_resultado = (saldo >= saque and saque <= limite) or not(saldo >= saque and saque >= limite)
print(print_resultado)