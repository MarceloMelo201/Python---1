'''

Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.

'''

from os import system 

system('clear')

lista_compras = []

while True:
    
    print('==== LISTA DE COMPRAS ====')
    print("1 - Inserir item\n2 - Apagar item\n3 - Listar itens\n4 - Sair")
    escolha = int(input('Digite a opção desejada: '))

    if escolha == 1:
        system('clear')
        novo_item = input("Item: ")
        lista_compras.append(novo_item) 
        
    if escolha == 2:
        system('clear')
        indice_str = input("Escolha um índice: ")

        try:
            indice = int(indice_str)
            del lista_compras[indice]

        except ValueError:
            print('Por favor digite número int.')

        except IndexError:
            print('Índice não existe na lista')
            
        except Exception:
            print('Erro desconhecido')
        
        


        

   



    
        

