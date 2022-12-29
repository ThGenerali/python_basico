print(''' 
      
      Dicionário
      
      ''')
#conjunto não ordenaddo de pares chave:valor, inde as chaves são únicas em uma dada instância do dicionário.
#Delimitados por chaves:{} e contém uma lista de pares chave:valor separada por vírgulas
print('''
      Criação Dict
      ''')
pessoa = {'nome': 'Guilerme', 'idade': 28}

pessoa = dict(nome='Guilherme', idade=28)

pessoa['telefone'] = '3333-1234'

print(pessoa)

print('''
      Acesso de Dados
      ''')

#valores são acessados e modificados pela chave
  
print(pessoa)
print(pessoa['nome'])

#dict aninhados
print('''
      dicts aninhados
      ''')

contatos = {
      'guilherme@gmail.com': {'nome': "Guilerme", 'telefone': '1234-4321'},
      'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '5214-4523'},
      'chappie@gmail.com': {'nome': 'Chappie', 'telefone': '5457-8541'}
}

print(contatos)
print(contatos['guilherme@gmail.com']['telefone'])

#iterar dicts
print('''
      íterar dicts
      ''')

for chave in contatos:
      print(chave, contatos[chave])
      
for chave, valor in contatos.items():
      print(chave, valor)