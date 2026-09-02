import os

os.system("cls")

N1 = float(input("Informe o 1º número: "))
N2 = float(input("Informe o 2º número: "))

print("""
    Código | Operação
    1      | +
    2      | -
    3      | /
    4      | *
    5      | STOP
""")

while True:
    escolha = input("Informe o código da operação: ")

    if escolha == "1":
        print(f"A soma dos números é: {N1 + N2}.")

    elif escolha == "2":
        print(f"A subtração dos números é: {N1 - N2}.")

    elif escolha == "3":
        if N2 == 0:
            print("Não é possível dividir por zero.")
        else:
            print(f"A divisão dos números é: {N1 / N2}.")

    elif escolha == "4":
        print(f"A multiplicação dos números é: {N1 * N2}.")

    elif escolha == "5":
        print("Operação encerrada.")
        break

    else:
        print("Código inválido.")