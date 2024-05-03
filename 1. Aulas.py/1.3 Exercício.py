from os import system

system("clear")

num1 = float(input("Digite o 1° inteiro: "))
num2 = float(input("Digite o 2° inteiro: "))

soma = num1 + num2
media = soma / 2
produto = num1 * num2

system("clear")

print("Média: {}".format(media))
print("Soma: {}".format(soma))
print("Produto: {}".format(produto))

if num1 > num2: 
    print("Maior valor: {}".format(num1))
    print("Menor valor: {}".format(num2))

elif num2 > num1:
    print("Maior valor: {}".format(num2))
    print("Menor valor: {}".format(num1))

elif num1 == num2:
    print("Os números são iguais: {}".format(num1))
