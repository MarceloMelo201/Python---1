'''

Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.

'''

from random import randint #Importando função da bibliotéca Random

num = randint (0, 5) #Sorteia um número

print("=== Tente descobrir o número escolhido ===")
escolha = int(input("Digite um número entre 0 e 5: ")) #Jogador tenta adivinhar

if escolha == num: #Caso acerte
    print("Número sorteado: {}".format(num))
    print("Número escolhido: {}".format(escolha))

    print("Você venceu!")

else: #Caso erre
    print("Número sorteado: {}".format(num))
    print("Número escolhido: {}".format(escolha))
    print("Você perdeu!")