from os import system

def notas():
    nota = []
    for i in range(4):
       
        nota.append(float(input(f"Digite a {i+1}ª nota: ")))

    for i in range(4):

        print(f"Nota {i+1}: {nota[i]}")

    media = sum(nota) / len(nota)
    print(f"Média: {media}")

    if media >= 7:
        print("Aprovado")
    
    elif media <7 and media >= 5:
        print("Recuperação")
    
    else:
        print("Reprovado")



notas()