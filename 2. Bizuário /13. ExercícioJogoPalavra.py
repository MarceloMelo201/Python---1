#faça um jogo para o usuário advinhar a palavra secreta 
#se a letra estiver na palavra, exibe, se não, exibe um asterisco

from os import system
from random import choice

system("clear")

palavra = ['amor', 'felicidade', 'lindo', 'programador', 'python']

palavra_escolhida = choice(palavra) 

codificador = len(palavra_escolhida) * '*'
tentativas = 0

acertos = list(codificador)

contador_de_acertos = len(palavra_escolhida)

while contador_de_acertos > 0: 

    letra_escolhida = input("Digite uma letra: ") #variavel é igual a letra que vai digitar
    texto_unificado = ''.join(acertos)

    if len(letra_escolhida) > 1:
        print("Digite apenas uma letra")
        tentativas += 1
        continue 

    if letra_escolhida in palavra_escolhida and letra_escolhida not in texto_unificado: 
        #se a letra digitada estiver na palavra escolhida

        posicao = palavra_escolhida.find(letra_escolhida) #posição onde a letra está

        acertos[posicao] = letra_escolhida #Acha a posição onde a letra está e muda o asterisco por ela

        texto_unificado = ''.join(acertos) #unifica a lista

        print(f"Palavra: {texto_unificado.upper()}") #print da palavra com as letras achadas 

        tentativas += 1
        contador_de_acertos -= 1
    
    elif letra_escolhida in texto_unificado:
         
         print(f"Palavra: {texto_unificado.upper()}")
         tentativas += 1

    else:
        print(f"Palavra: {texto_unificado.upper()}")
        tentativas += 1


system("clear")
print("=== VOCÊ GANHOU ===")
print(f"Palavra: {texto_unificado.upper()}")
print(f"Tentativas: {tentativas}")


        

        
       
        
