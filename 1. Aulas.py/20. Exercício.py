from os import system


def numeros():
    vetor = []

    for i in range(5):
        
        vetor.append(int(input(f"Digite o {i+1}º número: ")))

    
    maior = max(vetor)
    menor = min(vetor)

    system("clear")

    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")



numeros()