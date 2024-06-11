from dataclasses import dataclass
from os import system 

QUANTIDADE_ALUNOS = 2

@dataclass
class Aluno():
    nome: str
    idade: int
    peso: float
    altura: float


alunos = []

for i in range(QUANTIDADE_ALUNOS):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    peso =  float(input("Digite o peso: "))
    altura =  float(input("Digite a altura: "))
    aluno = Aluno(nome = nome, idade = idade, peso = peso, altura = altura)
    alunos.append(aluno)
    system("clear")

for dados_aluno in alunos:
    
    print(F"Nome: {dados_aluno.nome}")
    print(F"Idade: {dados_aluno.idade}")
    print(F"Peso: {dados_aluno.peso}")
    print(F"Altura: {dados_aluno.altura}\n")