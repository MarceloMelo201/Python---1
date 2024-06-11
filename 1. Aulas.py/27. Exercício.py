from dataclasses import dataclass
from os import system

QUANTIDADE_PET = 2

@dataclass
class Pet():
    nome: str
    idade: int
    raca: str
    porte: str
    alimentacao: str

pets = []

for i in range(QUANTIDADE_PET):

    nome = input("Digite o nome do pet: ")
    idade = int(input("Digite a idade: "))
    raca = input("Digite a raça: ")
    porte = input("Digite o porte: ")
    alimentacao = input("Digite a alimentação: ")
    pet = Pet(nome = nome, idade = idade, raca = raca, porte = porte, alimentacao = alimentacao)
    pets.append(pet)
    
    system("clear")

for dados_pet in pets:

    print(f"Nome {dados_pet.nome}")
    print(f"Idade {dados_pet.idade}")
    print(f"Raça {dados_pet.raca}")
    print(f"Porte {dados_pet.porte}")
    print(f"Alimentação {dados_pet.alimentacao}\n")

  
