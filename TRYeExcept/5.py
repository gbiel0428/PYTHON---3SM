import os
os.system("cls")

while True:
    try:
        saldo = float(input("Digite seu saldo: "))
        saque = float(input("Digite o valor do saque: "))

        if saque <= 0:
            print("O valor do saque deve ser maior que zero.")

        elif saque > saldo:
            print("Saldo insuficiente.")

        else:
            saldo -= saque
            print("Saque realizado com sucesso!")
            print(f"Saldo restante: {saldo}")
            break

    except ValueError:
        print("Informe apenas valores numéricos.")
