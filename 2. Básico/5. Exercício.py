"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

from os import system

system("clear")

num = input("Digite um número inteiro: ")

try:
    numInt = int(num)
    if (numInt % 2 == 0):
        print(f"O número {numInt} é par.")
    
    else:
        print(f"O número {numInt} é impar.")

except ValueError:
    print("Este valor não é um número inteiro")