import os
os.system("cls")

tarefa = [ ]

while True:
    print("\n")
    print("=== Menu ===")
    print("1 - Adicionar tarefa.")
    print("2 - Remover   tarefa.")
    print("3 - Mostrar   tarefa.")
    print("0 - Encerrar o Menu")
    op = int(input("Informe o Numero da Opção que Deseja Realizar: "))
    
    if op == 1:
        adicionar = input("Informe o Nome da Tarefa: ")
        tarefa.append(adicionar)
    elif op == 2:
        print(tarefa)
        remover = input("Informe o Nome da Tarefa que Deseja realizar:")
        tarefa.remove(remover)
    elif op == 3:
        print(tarefa)
    elif op == 0:
        print("Encerrando...")
        break
    else:
        print("Codigo Não Existente.")