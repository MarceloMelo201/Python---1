from os import system

'''
Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.

'''

nome = input("Digite seu nome completo: ")

print("Nome em maiúsculo: {}".format(nome.upper()))
print("Nome em minúsculo: {}".format(nome.lower()))
print("Numero de letras: {}".format(len(nome) - nome.count(' ')))

print("Número de letras do primeiro nome: {}".format(nome.find(' ')))