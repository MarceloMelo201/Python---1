'''
Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
 Para salários superiores a R$1250,00, calcule um aumento de 10%.
 Para os inferiores ou iguais, o aumento é de 15%.

'''

salario = float(input("Digite o valor do salário em R$: "))

if salario > 1250:
    aumento = salario * 1.1

else:
    aumento = salario * 1.15

print("Salário atual: R$ {}".format(salario))
print("Salário com aumento: R$ {}".format(aumento))
print("Total do aumento: R$ {}".format(aumento - salario))