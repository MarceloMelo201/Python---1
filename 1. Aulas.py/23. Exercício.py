from os import system

def soma(num_uno, num_duo):
    soma = num_uno + num_duo

    return soma

def subtracao (num_uno, num_duo):
    subtracao  = num_uno - num_duo

    return subtracao 

def multi(num_uno, num_duo):
    multi = num_uno * num_duo

    return multi

def divisao(num_uno, num_duo):
    divisao = num_uno / num_duo

    return divisao


num_uno = int(input("1º número: "))
num_duo = int(input("2º número: "))

print(f"Soma: {soma(num_uno, num_duo)}")
print(f"Subtração: {subtracao(num_uno, num_duo)}")
print(f"Multiplicação: {multi(num_uno, num_duo)}")
print(f"Divisão: {divisao(num_uno, num_duo)}")