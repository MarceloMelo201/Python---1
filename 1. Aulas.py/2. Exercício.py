from os import system

nome = input("Digite o nome: ")
sexo = input("Digite o sexo (M/F): ")
estado_civil = input("Digite seu estado cívil: ")

if (sexo.upper() == 'F' and estado_civil.upper() == 'CASADA'):
    tempo = int(input("Digite o tempo de casada: "))


print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado_civil}")
print(f"Tempo de casada: {tempo}")


