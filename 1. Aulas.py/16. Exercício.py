from os import system

soma = 0
notas = []

for i in range(3):
    notas.append(float(input(f"Digte a {i+1}ª nota: ")))
    soma += notas[i]

    
media = soma / 3

for nota in notas:
    print(f"Nota: {nota}")

print(f"Média: {media:.2f}")