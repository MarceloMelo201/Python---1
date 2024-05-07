"""
Iterando strings com while
"""
#       012345678910
#

import os

os.system("clear")

nome = 'Marcelo Melo'
contador = 0;

novoNome = ' '

tamanhoNome = len(nome)

while contador != tamanhoNome:
    letra = nome[contador]
    novoNome = f"&{letra}"

    contador += 1

    novoNome += '*'
    print(novoNome)
 