import random
sort = 0
lista = []
for cont in range (0,100):
    sort =  int(random.randint(-5,100))
    lista.append(sort)

print(f" Ordem da lista {sorted(lista)}")
