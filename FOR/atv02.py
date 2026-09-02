import os
import random
os.system("cls")

numeros = [ ]

for i in range(10):
    nome = input(f"Digite o {i+1}° Numero: ")
    numeros.append(nome)
    os.system("cls")
    
sortear =random.choice(numeros)
print(f"O Número sorteado é: {sortear}")