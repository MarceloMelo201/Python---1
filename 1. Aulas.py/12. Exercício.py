from os import system
from time import sleep

soma = 0


while True:
    system("clear")
    nota_um = float(input("Digite a 1ª nota: "))
    nota_dois = float(input("Digite a 2ª nota: "))

    if nota_um < 0 or nota_um > 10 or nota_dois < 0 or nota_dois > 10:
       print("Digite uma nota válida...")
       sleep(1)
       continue
        else:
            soma += nota_um
            soma += nota_dois
            break

system("clear")
media = soma / 2

print(f"Média: {media}")


