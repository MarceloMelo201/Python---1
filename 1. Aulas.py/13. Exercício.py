from os import system
from time import sleep

for i in range(3):
    while True:
        nota = float(input("Digite a {i+1}ª nota: "))

        if nota < 0 or nota > 10:
            print("Digite uma nota válida...")
            sleep(1)
            continue
        else:
            soma += nota
            break

media = soma / 3

print(f"Média: {media}")

if media >=7:
    print("Aprovado")

if media <7 and media >= 5:
    print("Recuperação")

else:
    print("Reprovado")