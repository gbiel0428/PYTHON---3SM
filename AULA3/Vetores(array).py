import os
os.system("cls")

numeros = [33 , 11 , 22 , 54 , 51 , 52, 17,33]
nomes= ["Julia", "Maria" , "Luiza" , "Enzo"]
#          0        1         2        3

#Adicionar um numero do vetor no ultimo lugar

numeros.append(67)
# Adicionar um elemento no vetor em um determinado lugar.

numeros.insert(3,50)
print(numeros)

# Remove um elemento que deseja.

numeros.remove(54)
print(numeros)
# Remove um elemento na posição.

numeros.pop(2)
print(numeros)

# SORT colocar  OS ELEMENTOS em ordem.

numeros.sort()
print(numeros)
nomes.sort()
print(nomes)

# Reverse  e ao contrario do sort.(gira ex: primeiro vira o ultimo)

numeros.reverse()
print(numeros)


# len - informa quantos valores existem dentro do vetor
# count - informa a quantidade de  um valor especifico.

qunt = len(nomes)
quantidade = numeros.count(33)
print(f"A quantidade de Números 33 que existe é: {quantidade}")
print(f"A quantidade de Nomes é: {qunt}")

# sum - somar dos Números

soma = sum(numeros)
print(f"A soma de todos os Números é: {soma}")



