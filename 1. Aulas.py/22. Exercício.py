from os import system 


def cabeca():
    system("clear")

    print("=== SENAI ===")


vetor = []


for i in range(5):
    cabeca()
    vetor.append(int(input("Digite o número: ")))

    if vetor[i] < 0:
        vetor[i] = 0


cabeca()

for i in range(5):
    print(f"Valor: {vetor[i]}")

    


