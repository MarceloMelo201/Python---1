from os import system

contador = 0

while contador == 0:

    system("clear")
    nota = int(input(f"Digite a 1ª nota: "))

    if nota <0 or nota > 10:

        print("Digite uma nota válida: ")

        continue

    nota2 = int(input("Digite a 2ª nota: "))

    if nota2 <0 or nota2 > 10:

        print("Digite uma nota válida: ")
        continue

    contador = 1

media = (nota + nota2) / 2

system("clear")
print(f"Média: {media}")