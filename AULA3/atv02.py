import os 
os.system("cls")

N1 = float(input("Informe o 1 Número: "))
N2 = float(input("Informe o 2 Número: "))

print("""
    Codigo | Operação
    1      |  +
    2      |  -
    3      |  /
    4      |  *
    5      |  STOP""")


while True:
    escolha = input("Informe o Codigo da operação: ")
    
    if escolha == "1":
        print(f"A Soma dos Números é: {N1 + N2}.")
    elif escolha == "2":
        print(f"A subtração dos Números é: {N1 - N2}.")
    elif escolha == "3":
        print(f"A Divisão dos Números é: {N1 / N2}.")
    elif escolha == "4":
        print(f"A Multiplicação dos Números é: {N1 * N2}.")
    elif escolha == "5":
        print("Operação Encerrada.")
        break
    else:
        print("Codigo Invalido.")
        













# match opcao:
#     case "1":
#         print(f"A soma dos Numeros é : {N1 + N2}.")
#     case "2":
#         print(f"A subtração dos Números é: {N1 - N2}.")
#     case "3":
#         print(f"A divisão dos Números é: {N1 / N2}.")
#     case "4":
#         print(f"A Multiplicação dos Números é: {N1 * N2}.")
#     case _:
#         print("Operação invalida")