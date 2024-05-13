from os import system

contador = 0
soma = 0

while True:
    nota = float(input("Digite uma nota: "))
    soma += nota
    contador += 1
    escolha = input("Deseja inserir mais uma nota(N = Sair) ").upper()

    if escolha == 'N':
        media = soma / contador 
        break
    else:
        continue


print(f"Média: {media}")