import os
os.system("cls")

numeros = [ ]

for i in range(6):
    n1 = int(input(f"informe o {i + 1}° Numero: "))
    numeros.append(n1)
    
soma = sum(numeros)
maior = max(numeros)
menor = min(numeros)
numeros.sort()


print(f"A soma dos Numeros é: {soma}")
print(f"O Maior dos Numeros é: {maior}")
print(f"O Menor dos Numeros é: {menor}")
print("Os Numeros em Ordem Crescente São: ")
print(numeros)