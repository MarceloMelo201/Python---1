from dataclasses import dataclass
from os import system

QUANTIDADE_LIVROS = 2

@dataclass
class Livro():
    titulo: str
    autor: str
    numero_de_paginas: int
    preco: float


livros = []

for i in range(QUANTIDADE_LIVROS):

    titulo = input("Digite o título: ")
    autor = input("Digite o autor: ")
    numero_de_paginas = int(input("Digite o número de páginas: "))
    preco = float(input("Digite o preço: "))
    livro = Livro(titulo = titulo, autor = autor, numero_de_paginas = numero_de_paginas, preco = preco)
    livros.append(livro)
    system("clear")

for dados_livro in livros:

    print(f"Título: {dados_livro.titulo}")
    print(f"Autor: {dados_livro.autor}")
    print(f"Número de páginas: {dados_livro.numero_de_paginas}")
    print(f"Preco: {dados_livro.preco}\n")
