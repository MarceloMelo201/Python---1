'''
 Exercício
 Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

'''

valor = int(input("Digite um número: "))

if valor % 2 == 0:
    print("{} é par.".format(valor))

else:
    print("{} é impar.".format(valor))