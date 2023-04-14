print("Cadastro do 1° usuário")
nome1 = input("Nome do usuário 1: ")
alt1 = float(input(f"Altura do {nome1}: "))
peso1 = int(input(f"Peso do {nome1}: "))
print("Cadastro do 2° usuário:")
nome2 = input("Nome do 2° usuário: ")
alt2 = float(input(f"Altura do {nome2}: "))
peso2 = float(input(f"Peso do {nome2}: "))
if (peso1 > peso2):
    print(f"O usuário mais pesado é:  {nome1}")
elif (peso2 > peso1):
    print(f"O usuário mais pesado é:  {nome2}")
if (alt1 > alt2):
    print(f"O usuário mais alto é:  {nome1}")
elif (alt2 > alt1):
    print(f"O usuário mais alto é:  {nome2}")
