import os
os.system("cls")


while True:
    try:
        n1 = int(input("Informe o 1 Número: "))
        n2 = int(input("Informe o 2 Número: "))
        soma = n1 + n2
        break
    except ValueError:
        print("Informe apenas Números")

print(f"A soma dos Numeros é: {soma}")
