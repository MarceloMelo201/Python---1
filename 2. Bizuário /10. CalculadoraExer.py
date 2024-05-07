from os import system
from time import sleep


escolha = 1

system("clear")

while escolha != 0:

    numS1 = input("Digite o primeiro número: ")
    numS2 = input("Digite o segundo número: ")

    system("clear")

    print("=== Escolha a operação a ser realizada ===")
    print("(+) - 1\n(-) - 2\n(*) - 3\n(/) - 4")
    
    try:
        num1 = int(numS1)
        num2 = int(numS2)

        opera = int(input(": "))

        match opera:

            case 1:

                num3 = num1 + num2
                system("clear")
                print(f"Valor 1: {num1}\nValor 2: {num2}")
                print(f"Resultado da soma: {num3}")
                escolha = int(input("Deseja sair?\n(1) - Nova operação\n0 - Sair  "))
                
                if (escolha == 1):
                    sleep(1)
                    system("clear")
                    continue

                elif (escolha != 1 and escolha != 0):
                    print("Opção inválida. Saindo...")
                    sleep(1)
                    system("clear")
                    break

            

            case 2:

                num3 = num1 - num2
                system("clear")
                print(f"Valor 1: {num1}\nValor 2: {num2}")
                print(f"Resultado da diferença: {num3}")
                escolha = int(input("Deseja sair?\n(1) - Nova operação\n0 - Sair  "))

                if (escolha == 1):
                    sleep(1)
                    system("clear")
                    continue

                elif (escolha != 1 and escolha != 0):
                    print("Opção inválida. Saindo...")
                    sleep(1)
                    system("clear")
                    break
                
               
            case 3:

                num3 = num1 * num2
                system("clear")
                print(f"Valor 1: {num1}\nValor 2: {num2}")
                print(f"Resultado da multiplicação: {num3}")
                escolha = int(input("Deseja sair?\n(1) - Nova operação\n0 - Sair  "))
                
                if (escolha == 1):
                    sleep(1)
                    system("clear")
                    continue

                elif (escolha != 1 and escolha != 0):
                    print("Opção inválida. Saindo...")
                    sleep(1)
                    system("clear")
                    break

            case 4:

                num3 = num1 / num2
                system("clear")
                print(f"Valor 1: {num1}\nValor 2: {num2}")
                print(f"Resultado da divisão: {num3}")
                escolha = int(input("Deseja sair?\n(1) - Nova operação\n0 - Sair  "))
                
                if (escolha == 1):
                    sleep(1)
                    system("clear")
                    continue

                elif (escolha != 1 and escolha != 0):
                    print("Opção inválida. Saindo...")
                    sleep(1)
                    system("clear")
                    break

            case _:
                print("Opção inválida. Reiniciando...")
                sleep(1)
                continue





    except ValueError:
        system("clear")
        print("Digite uma opção válida de número. Reiniciando...")
        sleep(1)
        system("clear")
        continue 
        

