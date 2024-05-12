'''

Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa,
 mostrando em seguida o primeiro e o último nome separadamente.

'''

frase = input("Digite o seu nome: ")

palavras = frase.split()
print("Primeiro nome: {}".format(palavras[0]))
print("Último nome: {}".format(palavras[len(palavras) - 1]))
