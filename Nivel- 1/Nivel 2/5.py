import os
os.system("cls")

nomes = [ ]

while True:
    Cadastra =input("Informe o Seu Nome: (Informe Fim pra encerrar):")
    
    if Cadastra == "Fim":
        break
    else:
        nomes.append(Cadastra)

nomes.sort()
print("Nomes em Ordem Alfabetica: ")
print(nomes)

print(F"A quantidade de Nomes na Lista e : {len(nomes)}")