from os import system
pares = 0
impares = 0
system('clear')

for i in range(5):
    numeros = int(input(f"Digite o {i+1}º número: "))

    if numeros % 2 == 0:
        pares += 1
    else:
        impares += 1

system("clear")

print(f"Quantidade de pares: {pares}")
print(f"Quantidade de impares: {impares}")