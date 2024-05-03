from os import system
system("clear || cls")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

nota_uno = int(input("Digite a 1ª nota: "))
nota_duo = int(input("Digite a 2ª nota: "))


media = (nota_uno + nota_duo) / 2

system("clear || cls")

print("=== EXIBINDO RESULTADOS ===")
print("Nome: {}\nIdade: {}\n1ª nota: {}\n2ª nota: {}\nMédia: {}".format(nome, idade, nota_uno, nota_duo, media))
