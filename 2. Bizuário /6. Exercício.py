"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

"""
import os

os.system("clear")

hora = input("Digite a hora: ")

try:
    numHora = int(hora)
   

    if (numHora >= 0 and numHora <= 23):


        if (numHora >= 0 and numHora < 12):
            print("Bom-dia!");
        

        if (numHora >= 12 and numHora < 18):
            print("Boa-tarde!")

        else:
            print("Boa-noite!")

    else:
        print("Digite um horário válido.")

except:
    print("Digite um valor válido.")
