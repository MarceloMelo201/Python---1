from os import system 

system("clear")

idade = int(input("Digtite a sua idade: "))

if idade >= 18 and idade <= 65:
    
    print("Usuário obrigado a votar.")

else:
    print("Usuário não obrigado a votar.")