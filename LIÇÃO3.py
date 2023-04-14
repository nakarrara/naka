import random
lista = []

for cont in range (0,20):
    aux =  int(random.randint(1,35))
    lista.append(aux)

print(f" O maior número: {max(lista)}")
print(f" O menor número: {min(lista)}")
print(lista)