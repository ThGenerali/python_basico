contatos = {
      'guilherme@gmail.com': {'nome': "Guilerme", 'telefone': '1234-4321'},
      'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '5214-4523'},
      'chappie@gmail.com': {'nome': 'Chappie', 'telefone': '5457-8541'}
}
copia = contatos.copy() #copia para as demais demonstrações dos métodos

#clear
print('''
    {}.clear
    ''')

print(contatos)
print(contatos.clear())                 

#copy
print('''
    {}.copy
    ''')
print(copia)

#fromkeys
print('''
    {}.fromkeys
    ''')

print(dict.fromkeys(['nome', 'telefone']))
print(dict.fromkeys(['nome', 'telefone'], 'vazio'))

#get
print('''
    {}.get
    ''')

print(copia.get('chave'))
print(copia.get('guilherme@gmail.com'))

#items
print('''
    {}.items
    ''')

print(copia.items())

#keys
print('''
    {}.keys
    ''')

print(copia.keys())

#pop
print('''
    {}.pop
    ''')

print(copia.pop('giovanna@gmail.com'))
print(copia.pop('giovanna@gmail.com', {}))

#popitem
print('''
    {}.popitem
    ''')

print(copia.popitem())

#setdefault
print('''
    {}.setdefault
    ''')

print(copia.setdefault('nome', 'giovanna'))
print(copia.setdefault('idade', 28))

#update
print('''
    {}.update
    ''')

copia.update({'chappie@gmail.com': {'nome': 'chappie', 'telefone': '3214-8542'}})
print(copia)

#values
print('''
    {}.values
    ''')

print(copia.values())

#in
print('''
    in
    ''')

print('chappie' in copia['chappie@gmail.com']['nome'])
print('megui@gmail.com' in copia)

#del
print('''
    del
    ''')

del copia['nome']
del copia['idade']
print(copia)