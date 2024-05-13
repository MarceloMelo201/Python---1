from os import system
from time import sleep

soma = 0

for i in range(3):
    while True:
        nota = float(input(f"Digite a {i+1}ª nota: "))

        if nota < 0 or nota > 10:
            print("Digite uma nota válida...")
            sleep(1)
            continue
        else:
            soma += nota
            break

media = soma / 3

print(f"Média: {media:.2f}")

if media >= 7:
    print("Aprovado")

elif media >=5 and media < 7:
    print("Recuperação")

else:
    print("Reprovado")