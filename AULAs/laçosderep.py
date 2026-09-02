import os
os.system("cls")


carrinho = []

while True:
    produto=float(input("Informe o valor do produto: "))
    if (produto == 0 ):
        break
    else:
        carrinho.append(produto)


lsita= len(carrinho)
total = sum(carrinho)

print(f"A lista dos preços é: R$: ")
print(f"O valor total da compra e R$: {total:.2f}")