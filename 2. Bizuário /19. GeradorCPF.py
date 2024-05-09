"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890) 
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7

"""

from os import system 

system("clear")

soma_cpf = 0

j = 10


while True:

    cpf = input("Digite o seu cpf para validação: ")

    cpf_separado = [int(digito) for digito in str(cpf)]
    
    if len(cpf_separado) > 9:
       print('Digite uma opção válida.')

    
    for i in range(9): 
        soma_cpf += cpf_separado[i] * j
        j -= 1

    multi_cpf = soma_cpf * 10
    resto = multi_cpf % 11
        
    if resto > 9:
        resultado = 0
        print(f"Primeiro dígito: {resultado}")

    else:
         resultado = resto
         print(f"Primeiro dígito: {resultado}")

    
    
    



