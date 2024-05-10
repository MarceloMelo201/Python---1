from os import system
system("clear")
soma = 0
for i in range(5):
    soma += int(input(f"Digite o {i+1}º número: "))
    
system("clear")
print(f"Soma dos números: {soma}")

