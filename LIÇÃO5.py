import random

inicio = 0
media = 0
aux = 0
lista = []
listaI = []
listaP = []
while (inicio <= 100):

    aux = int(random.randint(-10, 38))
    media += aux
    lista.append(aux)
    if (aux % 2 == 1):
        listaI.append(aux)
    if (aux % 2 == 0):
        listaP.append(aux)
    inicio += 1
print(f" A média é {round((media / inicio), 2)}")
print(f" A soma de 1 a 100 é: {sum(lista)}")
print(f" A soma dos pares é: {sum(listaP)}")
print(f" A soma dos impares é:  {sum(listaI)}")