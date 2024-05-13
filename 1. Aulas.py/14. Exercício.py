from os import system

contador = 0
soma = 0

while True:

    nota = float(input("Digite uma nota: "))
    soma += nota
    contador += 1

    escolha = input("Deseja inserir mais uma nota(N = Sair) ").upper()

    if escolha == 'N':

        break

    else:

        continue

media = soma / contador 
print(f"Média: {media}")

if media >= 7:
    print("Aprovado")

elif media >=5 and media < 7:
    print("Recuperação")

else:
    print("Reprovado")