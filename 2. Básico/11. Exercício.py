'''
Programa que analisa uma frase, conta a quantidade de cacacteres e o número de repetições 
imprime na tela o caractere que mais aparece e a quantidade de aparições.

'''

frase_velha = 'O Python é uma linguagem de programação  multiparadigma. Python foi criado por Guido van Rossum.'


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