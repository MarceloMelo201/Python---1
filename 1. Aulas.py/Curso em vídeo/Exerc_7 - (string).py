'''

Exercício Python 26: Faça um programa que leia uma frase pelo teclado e
 mostre quantas vezes aparece a letra “A”,
em que posição ela aparece a primeira vez e
em que posição ela aparece a última vez.

'''

frase = str(input("Digite uma frase: ")).upper()

print("Número de vezes que o 'a' aparece: {}".format(frase.count('A')))
print("Primeira posição que aparece: {}".format(frase.find('A')))
print("Primeira posição que aparece: {}".format(frase.find('A') + 1))
print("Primeira posição que aparece: {}".format(frase.rfind('A') + 1))
