import os
os.system("cls")

protudos = []

for i in range(5):
    adicionar = input("Informe o Nome do Produto: ")
    protudos.append(adicionar)


    
print(f"Os protudos São : {protudos}")
print(f"A quantidade de Produtos Cadastratos São: {len(protudos)}")