from os import system
system("clear")

soma = 0
for i in range(4):
    soma += int(input(f"Digite a {i+1}ª nota: "))
    

media = soma / 4
system("clear")

print(f"Média: {media}")
