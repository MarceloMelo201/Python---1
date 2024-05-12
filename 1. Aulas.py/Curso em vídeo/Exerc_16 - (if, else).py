'''

Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e
 diga ao usuário se elas podem ou não formar um triângulo.

'''

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

if a + b > c and b + c > a and a + c > b:
    print("Os três valores de reta formam um triângulo.")

else:
    print("Os três valores de reta não formam um triângulo.")