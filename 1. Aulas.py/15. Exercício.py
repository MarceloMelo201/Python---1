from os import system
from time import sleep

soma = 0
contador = 0

while True:

    system("clear")
    nota = float(input("Digite a nota: "))
    soma += nota
    contador += 1

    print("S - inserir mais uma nota\nP - Ver quantidade de notas\nN - Calcular Média")
    escolha = input("Digite a escolha: ").upper()


    if escolha == 'S':
        system("clear")
        continue

    elif escolha == 'P':
        system("clear")
        print(f"Quantidade de notas inseridas: {contador}")
        input("Pressione enter para continuar...")
        continue

    elif escolha == 'N':
        system("clear")
        break

    else:
        print("Opção inválida...")
        sleep(1)
        break


media = soma / contador

system("clear")
print(f"Média: {media:.2f}")




