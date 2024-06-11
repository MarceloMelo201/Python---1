from dataclasses import dataclass

@dataclass
class Aluno():
    nome: str
    idade: int


alunos = []

for i in range(4):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    aluno = Aluno(nome = nome, idade = idade)
    alunos.append(aluno)

for dados_aluno in alunos:
    print(f"Nome: {dados_aluno.nome}")
    print(f"Idade: {dados_aluno.idade}")