"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Digite seu nome:  ")

nomeLido = len(nome)

if nomeLido <= 4:
    print("Seu nome é muito curto")

elif nomeLido > 4 and nomeLido < 7:
    print("Seu nome é normal")

else:
    print("Seu nome é muito grande")