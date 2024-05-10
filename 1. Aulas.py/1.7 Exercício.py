from os import system 


while True:
    
    try:
        system("clear")
        nome = input("Digite o nome do produto: ")
        quantidade_adiquirida = int(input("Digite a quantidade adiquirida: "))
        preço_unidade = float(input("Preço por unidade: "))

        total = quantidade_adiquirida * preço_unidade

        if quantidade_adiquirida <= 5:
            desconto = total * (2/100)

        elif quantidade_adiquirida > 5 and quantidade_adiquirida <= 10:
            desconto = total * (3/100)

        elif quantidade_adiquirida > 10:
            desconto = total * (5/100)

        total_a_pagar = total - desconto

        print(f"Nome do produto: {nome}")
        print(f"Total: {total}")
        print(f"Desconto: {desconto}")
        print(f"Total a pagar: {total_a_pagar}")
        continuar = input("Pressione enter para continuar...")

    except ValueError:
        print("Digite um valor válido.")
