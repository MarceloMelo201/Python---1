from os import system

system("clear")
soma = 0

for i in range(3):
    soma += int(input(f"Digite a {i+1}ª nota: "))

media = soma / 3

system("clear")

print("Média: {:.2f}".format(media))

if media >= 7:
    print("Aprovado.")

elif media > 4 and media < 7:
    print("Recuperação.")

else:
    print("Reprovado.")