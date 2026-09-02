import os
os.system("cls")


while True:
    try:
        idade = int(input("Informe a Sua Idade: "))
        if idade >=18:
            print(F"Sua Idade é: {idade}, então voçê e Maior de Idade.")
        else:
            print(f"Sua Idade é: {idade}, então você e Menor de Idade.")
        break
    except ValueError:
        print("Informe apenas Números para consultar a sua Idade.")