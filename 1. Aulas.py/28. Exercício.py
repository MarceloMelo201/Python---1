from dataclasses import dataclass
from os import system

QUANTIDADE_CLIENTE = 1

@dataclass
class Veiculo():
    placa: str
    cor: str
    numero_passageiros: int
    capacidade_tanque: int
    velocidade_maxima: float
    consumo_medio: float


@dataclass
class Cliente():
    nome: str
    idade: int
    cpf: str
    endereco: str
    telefone: str

clientes = []
veiculos = []

for i in range(QUANTIDADE_CLIENTE):

    system("clear")

    print("=== INFORMAÇÕES DO CLIENTE ===\n")

    nome = input("Digite o nome do cliente: ")
    idade = int(input("Digite a idade: "))
    cpf = input("Digite o CPF: ")
    endereco = input("Digite o endereço: ")
    telefone = input("Digite o telefone: ")

    cliente = Cliente(nome = nome, idade = idade, cpf = cpf, endereco = endereco, telefone = telefone)
    clientes.append(cliente)

    system("clear")

    print("=== INFORMAÇÕES DO VEÍCULO ===\n")

    placa = input("Digite a placa do veículo: ")
    cor = input("Digite a cor do veículo: ")
    numero_passageiros = int(input("Digite o número de passageiros: "))
    capacidade_tanque = int(input("Digite a capacidade do tanque: "))
    velocidade_maxima = float(input("Digite a velocidade máxima do veículo: "))
    consumo_medio = float(input("Digite o consumo médio: "))

    veiculo = Veiculo(placa = placa, cor = cor, numero_passageiros = numero_passageiros, capacidade_tanque = capacidade_tanque, velocidade_maxima = velocidade_maxima, consumo_medio = consumo_medio)
    veiculos.append(veiculo)

    system("clear")

for dados_cliente in clientes:

    print("=== CLIENTE === ")
    print(f"Nome: {dados_cliente.nome}")
    print(f"Idade: {dados_cliente.idade}")
    print(f"CPF: {dados_cliente.cpf}")
    print(f"Endereço: {dados_cliente.endereco}")
    print(f"Telefone: {dados_cliente.telefone}\n")

for dados_veiculo in veiculos:

    print("=== VEÍCULO ===")

    print(f"Placa: {dados_veiculo.placa}")
    print(f"Cor: {dados_veiculo.cor}")
    print(f"Números de passageiros: {dados_veiculo.numero_passageiros}")
    print(f"Capacidade do tanque: {dados_veiculo.capacidade_tanque}")
    print(f"Velocidade Máxima: {dados_veiculo.velocidade_maxima}")
    print(f"Cconsumo médio: {dados_veiculo.consumo_medio}")
