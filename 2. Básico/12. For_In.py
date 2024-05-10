
texto = 'Python'

novo_texto = ''

for letra in texto: #Para cada letra no texto
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')

"""
For + Range
range -> range(start, stop, step)
"""
numeros = range(0, 100, 8)

for numero in numeros: #Para cada iteração um valor é atribuido a variável 'numero' dentro do range
    print(numero)