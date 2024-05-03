from os import system
system("cls || clear")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

nota_uno = int(input("Digtie a 1ª nota: "))
nota_duo = int(input("Digtie a 2ª nota: "))
nota_tri = int(input("Digite a 3ª nota: "))

media = (nota_uno + nota_duo) / 2

system("cls || clear")

print("Nome: {}".format(nome))
print("Idade: {}".format(idade))
print("1ª nota: {}".format(nota_uno))
print("2ª nota: {}".format(nota_duo))
print("3ª nota: {}".format(nota_tri))

if media >= 7: 
    print("Aprovado")

else: 
    print("Reprovado")