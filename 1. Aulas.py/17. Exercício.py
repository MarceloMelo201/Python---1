from os import system

valor = []

for i in range(5):
    valor.append(int(input(f"Digite o {i+1} valor: ")))


system("clear")
for i in range(len(valor)):
    print(f"Valor: {valor[i]}")


maior_valor = max(valor)
menor_valor = min(valor)
print(f"Maior valor: {maior_valor}")
print(f"Menor valor: {menor_valor}")