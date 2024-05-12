from math import pow, sqrt, trunc

num1 = float(input("Digite o cateto oposto: "))
num2 = float(input("Digite o cateto adjacente: "))

raiz1 = pow(num1, 2)
raiz2 = pow(num2, 2)

hipo = raiz1 + raiz2
hipofinal = sqrt (hipo)

print("A hipotenusa é: {}".format(trunc(hipofinal)))