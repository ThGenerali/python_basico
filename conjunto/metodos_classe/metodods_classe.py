conjunto_a = {1, 2, 3, 9, 8}
conjunto_b = {2, 3, 4}
conjunto_c = {4, 1, 2, 5, 6, 3}
conjunto_d = {10, 21}

print('conjunto_a =', conjunto_a,'conjunto_b =', conjunto_b,'conjunto_c =', conjunto_c,'conjunto_d =', conjunto_d)

print(f''''
    union
    (conjunto_a e conjunto_b)
    {conjunto_a.union(conjunto_b)}
''')

print(f''''
    intersection
    (conjunto_a e conjunto_b)
    {conjunto_a.intersection(conjunto_b)}
''')

print(f''''
    difference
    (conjunto_a e conjunto_b)
    {conjunto_a.difference(conjunto_b)}
    {conjunto_b.difference(conjunto_a)}
''')

print(f''''
    symmetric_difference
    (conjunto_a e conjunto_b)
    {conjunto_a.symmetric_difference(conjunto_b)}
''')

print(f''''
    issubset
    (conjunto_b e conjunto_c)
    {conjunto_b.issubset(conjunto_c)}
    {conjunto_c.issubset(conjunto_b)}
''')

print(f''''
    issuperset
    (conjunto_b e conjunto_c)
    {conjunto_b.issuperset(conjunto_c)}
    {conjunto_c.issuperset(conjunto_b)}
''')

print(f''''
    isdisjoint
    (conjunto_a , conjunto_b e conjunto_d)
    {conjunto_a.isdisjoint(conjunto_d)}
    {conjunto_a.isdisjoint(conjunto_b)}
''')

sorteio = {2, 3, 1}
print(sorteio)
print(f''''
    add
''')
sorteio.add(25)
print(sorteio)

print(f''''
    clear
''')
sorteio_copy = sorteio.copy()
sorteio_copy.clear()
print(sorteio_copy)

print(f''''
    copy
''')
sorteio_copy = sorteio.copy()
print(sorteio_copy, sorteio)

print(f''''
    discard
''')
sorteio.discard(1)
sorteio.discard(45)
print(sorteio)

print(f''''
    pop
''')
sorteio.pop()
print(sorteio)

print(f''''
    remove
''')
sorteio.remove(25)
print(sorteio)

print(f''''
    len
    {len(sorteio)}
''') 

print(f''''
    in
    {1 in sorteio}
''')
