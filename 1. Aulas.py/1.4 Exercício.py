from os import system 

system("clear")
login = input("Digite o login: ")
senha = input("Digite a senha: ")

nome = 'Marcelo'
verificação = 'striker201'

system("clear")

if login == nome and senha == verificação:
    print("Bem-vindo!")

else:
    print("Acesso não autorizado, login ou senha inválidos.")