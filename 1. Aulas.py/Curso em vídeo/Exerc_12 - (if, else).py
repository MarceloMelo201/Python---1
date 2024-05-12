'''
Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200Km e
 R$0,45 parta viagens mais longas.

'''

dist = float(input("Digite a distância em Km: "))

if dist <= 200:
    valor = 0.5 * dist
    print("O valor total da viagem é: R$ {}".format(valor))

else:
    valor = 0.45 * dist
    print("O valor total da viagem é: R$ {}".format(valor))