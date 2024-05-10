from os import system 

def limpar_tela():
    system("clear")


limpar_tela()

valor_uno = input("Digite o primeiro valor: ")
valor_duo = input("Digite o segundo valor: ")
escolha = input("Escolha a operação:\n(+) - 1\n(-) - 2\n(*) - 3\n(/) - 4")

limpar_tela()

try:
    opera = int(escolha)

    if opera > 0 and opera < 4:
        
        primeiro_valor = int(valor_uno)
        segundo_valor = int(valor_duo)
        

        if opera == 1:
            resultado = primeiro_valor + segundo_valor
        
        elif opera ==2:
            resultado = primeiro_valor - segundo_valor

        elif opera == 3:
            resultado = primeiro_valor * segundo_valor

        elif opera == 4:
            resultado = primeiro_valor / segundo_valor

        print(f"Resultado da operação: {resultado}")

except ValueError:
    print('Por favor digite número int.')

except Exception:
    print('Erro desconhecido')
        
