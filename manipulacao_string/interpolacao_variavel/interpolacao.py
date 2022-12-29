nome = "Thiago"
idade = 19
meta = "desenvolvedor de ia"
linguagem = "Python"

#old style %
print("Olá, me chamo %s. Tenho %d anos, quero me tornar um %s e estudo a linguagem %s" % (nome, idade, meta, linguagem))

#modo format
print("Olá, me chamo {}. Tenho {} anos, quero me tornar um {} e estudo a linguagem {}".format(nome, idade, meta, linguagem))
#precisa informar as variáveis em ordem para serem selecionadas corretamente

print("Olá, me chamo {3}. Tenho {0} anos, quero me tornar um {2} e estudo a linguagem {1}".format(idade, linguagem, meta, nome))
#pode selecionar as variáveis pelo sem indice, não precisa colocalas em ordem

print("Olá, me chamo {nome}. Tenho {idade} anos, quero me tornar um {meta} e estudo a linguagem {linguagem}".format(nome = nome, idade = idade, meta = meta, linguagem = linguagem))
#pode colocar nomes de identificação entre as chaves e depois voce pode atribuir o valor das variáveis em cada nome de identificação

#objeto
pessoa = {"nome": "Thiago", "idade": 19, "meta": "desenvolvedor de ia", "linguagem" : "Python"}
print("Olá, me chamo {nome}. Tenho {idade} anos, quero me tornar um {meta} e estudo a linguagem {linguagem}".format(**pessoa))
#seleciona as propriedades do objeto

#f-string
print(f"Olá, me chamo {nome}. Tenho {idade} anos, quero me tornar um {meta} e estudo a linguagem {linguagem}")

#formatar stings com f-string
PI = 3.14159

print(f"valor de PI: {PI:.2f}")
#2f é a propriedade que define o tanto de casas decimais que irá aparecer

print(f"valor de pi: {PI:10.2f}")
#10 define o tamanho da variável com mais 10 caracteres

