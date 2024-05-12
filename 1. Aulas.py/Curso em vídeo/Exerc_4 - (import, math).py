from math import cos, sin, tan, radians

ang = float(input("Digite um ângulo: "))

rad = radians(ang)

seno = sin(rad)
coss = cos(rad)
tang = tan(rad)

print("O seno é: {:.2f}\nO cosseno é: {:.2f}\nA tangente é: {:.2f}".format(seno, coss, tang))