from os import system

def numeros():
    numero = []
    positivos = []
    negativos = []

    for i in range(10):

        numero.append(int(input(f"Digite o {i+1}º número: ")))

        if numero[i] > 0:
            positivos.append(numero[i])

        else:
            negativos.append(numero[i])

    
    system("clear")
    print(f"Quantidade de negativos: {len(negativos)}")
    print(f"Soma dos positivos: {sum(positivos)}")


numeros()