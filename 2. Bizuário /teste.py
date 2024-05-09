



from os import system 
system("clear")

soma_cpf = 0
j = 10

while True:

    cpf = int(input("Digite o seu cpf para validação: "))
    cpf_separado = [int(digito) for digito in str(cpf)]

    if len(cpf_separado) > 9:
       print('Digite uma opção válida.')
       continue

    for i in range(9):
        soma_cpf += cpf_separado[i] * j
        j -= 1
    
    multi_cpf = soma_cpf * 10

    print(multi_cpf)




