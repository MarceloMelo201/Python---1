# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.
from os import system

def multi(numero):
    resultado = 1
    contador = len(numero)
    for i in range(contador):
        resultado *= numero[i] 

    return (f"Resultado: {resultado}")

   
numero = []
escolha = 0

while escolha == 0:
    
    for i in range(4):
        numero.append(int(input("Digite um número: ")))
    
    escolha = int(input("Sair?\n(1)- Sim\n(0) - Não  "))
    system("clear")

print(multi(numero))

