import os

os.system("clear")

num = int(input("Digite um número: "))

for i in range(10):
    print(f"{num} X {i+1} = {num * (i+1)}")