from os import system

valor = []

pares = 0
impares = 0

for i in range(6):
    valor.append(int(input(f"Digite o {i+1}º valor: ")))

    if valor[i] % 2 == 0:
        pares +=1
    
    else:
        impares += 1


for i in range(len(valor)):
    print(f"Valor: {valor[i]}")

print(f"Quantidade de pares: {pares}")
print(f"Quantidade de impares: {impares}")
