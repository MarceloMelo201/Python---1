#Variáveis

'''

int = Inteiro 
float = quebrado
str = string
bool = booleano (verdadeiro/falso)

'''


#Dinâmica

nome = "Celo"
idade = 20
peso = 62.500


#Variáveis no meio da frase:

'''
.format(variável)

print(" {} {} {}".format(nome, idade, peso))

'''

#Estática 

nome: str = "Celo"
idade: int = 20
peso: float = 62.500

"""
print(f"Nome : {nome}")
print(f"Idade : {idade}")
print(f"Peso : {peso}")

maior = max(num1, num2)
menor = min(num1, num2)

"""

#String

'''

frase = "Curso em video Python"

frase[9] == aparece o 13 caractere

frase[9:13] == do 9 até o 12

frase[9:21:2] == do 9 até o 20 pulando de 2 em 2

frase[:5] == do 0 ao 4

frase[5:] == do 5 até o final


'''

#string - análise

'''

len(frase) == diz quantos caracteres tem

frase.count('o') == conta quantas vezes existe a letra 'o'
    frase.count('o',0,13) == conta do 0 ao 13

frase.find('deo') == encontra o "deo" e diz em qual local ele começa 
    se aparecer -1 é porque não foi encontrado

'curso' in frase == true ou false / se tem a palavra curso dentro de "frase"

frase.replace('python', 'Android') == procura a palavra 1 e troca pela 2

frase.upper() == em maiúsculo 

frase.capitalize() == tudo em minúsculo menos a primeira letra (fica em maiúsculo)

frase.title() == 'capitalize' palavra por palavra

frase.strip() == remove espaços inúteis 
    frase.rstrip() == apenas na direita  
    frase.lstrip() == apenas na esquerda 

frase.split() == divide em espaços (gera uma lista separando todas as palavras)

'''


#Desvios condicionais 

'''
'''