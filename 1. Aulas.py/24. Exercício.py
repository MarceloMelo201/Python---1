
def preco():
    preco = float(input("Digite o valor do produto: "))
    return preco

def infla(preco):

    if preco > 100:

        preco_inflado = preco * 1.20
    
    else:

        preco_inflado = preco * 1.10
    
    return preco_inflado


preco_uno = preco()
resultado = infla(preco_uno)

print(f"Preço inflado: {resultado}")