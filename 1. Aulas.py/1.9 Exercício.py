from os import system

def limpar_tela():
    system('clear')

limpar_tela()

valor_uno = input("Digite o primeiro valor: ")
valor_duo = input("Digite o segundo valor: ")

try:
    valor_uno = int(valor_uno)
    valor_duo = int(valor_duo)

    escolha = int(input("Escolha a operação:\n(+) - 1\n(-) - 2\n(*) - 3\n(/) - 4\n: "))

    match(escolha):
        
        case 1:
            resultado = valor_uno + valor_duo
        
        case 2:
            resultado = valor_uno - valor_duo
        
        case 3:
            resultado = valor_uno * valor_duo
        
        case 4:
            resultado = valor_uno / valor_duo
            
        case _:
            print("Digite um valor válido...")

    limpar_tela()
    print(f"Primeiro valor: {valor_uno}")
    print(f"Segundo valor: {valor_duo}")
    print(f"Resultado: {resultado}")

except:
    limpar_tela()
    print("Digite um valor válido.")