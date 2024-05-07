frase_velha = 'O Python é uma linguagem de programação  multiparadigma. Python foi criado por Guido van Rossum.'

#Achar uma maneira de remover os espaços e verificar a maior letra repetida 

from os import system

system("clear")

nova_frase = frase_velha.replace(" ", '')

i = 0 

repetidor = 0

while i < len(nova_frase):
    
    letra_atual = nova_frase[i]
    nova_frase.count(letra_atual) 

    
    if (nova_frase.count(letra_atual)) > repetidor:

        repetidor = nova_frase.count(letra_atual)

        letra_mais_repetida = letra_atual
        

    i += 1


print(f"Letra mais repetida: {letra_mais_repetida}\nRepetições: {repetidor}")