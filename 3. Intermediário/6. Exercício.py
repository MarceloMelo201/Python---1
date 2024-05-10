# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

from os import system 

def duplicar(x):

    def triplicar(x):

        def quadruplicar(x):
            numero = x * 4
            return (f"Número quadruplicado: {numero}")
        

        numero = x * 3
        print(quadruplicar(x))
        return (f"Número triplicado: {numero}")
    
    numero = x * 2
    print(triplicar(x))
    return (f"Número duplicado: {numero}")


x = int(input("Digite um número: "))

print(duplicar(x))

