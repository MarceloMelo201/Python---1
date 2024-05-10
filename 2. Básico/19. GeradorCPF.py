from os import system



#função para limpar a tela
def limpar_tela():
    system("clear")


def validar_cpf(cpf):
    cpf_separado = [int(digito) for digito in cpf if digito.isdigit()]
    if len(cpf_separado) != 9:
        return "CPF inválido. Deve conter apenas 9 dígitos"
    
    multiplicador = 10
    soma_cpf = 0
    for i in range(9):
        soma_cpf += cpf_separado[i] * multiplicador 
        multiplicador -= 1

    digito_um = (soma_cpf * 10) % 11
    if digito_um == 10:
        digito_um = 0

    cpf_separado.append(digito_um)

    multiplicador = 11
    soma_cpf_dois = 0
    for i in range(10):
        soma_cpf_dois += cpf_separado[i] * multiplicador
        multiplicador -= 1

    digito_dois = (soma_cpf_dois * 10) % 11
    if digito_dois == 10:
        digito_dois = 0

    return f"1º Dígito: {digito_um}\n2º Dígito: {digito_dois}" 

    



while True:
    limpar_tela()
    print("=== VALIDAÇÃO DE CPF === ")
    cpf = input("Digite o seu CPF para validação (somente números): ")
    resultado = validar_cpf(cpf)
    print(resultado)
    input("Pressione Enter para continuar...")

    
        



