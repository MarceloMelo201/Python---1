'''

Exercício Python 29: Escreva um programa que leia a velocidade de um carro.
 Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
  A multa vai custar R$7,00 por cada Km acima do limite.

'''

velo = float(input("Digite a velocidade atual do carro (Km/h): "))

if velo > 80:
    multa = (velo - 80) * 7

    print("Você foi multado!")
    print("Valor da multa R$: {:.2f} reais".format(multa))

else:
    print("Velocidade dentro dos limites da pista.")
