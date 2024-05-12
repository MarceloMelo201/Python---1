'''
Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

'''
from sys import maxsize

valor = [0] * 3
menor = maxsize
maior = - maxsize

for i in range(3):
    valor[i] = int(input("Digite o {} valor: ".format(i + 1)))
    if valor[i] > maior:
        maior = valor[i]

    if valor[i] < menor:
        menor = valor[i]

print("Maior valor: {}\nMenor Valor: {}".format(maior, menor))