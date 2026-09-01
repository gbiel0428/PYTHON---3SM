import os
os.system("cls")

notas = []

while True:
    nota = float(input("Digite uma nota (-1 para encerrar): "))

    if nota == -1:
        break

    notas.append(nota)

print("\nNotas cadastradas:")

for nota in notas:
    print(nota)

if notas:
    print(f"Quantidade: {len(notas)}")
    
    print(f"Média: {sum(notas) / len(notas):.2f}")
    
    print(f"Maior nota: {max(notas)}")
    
    print(f"Menor nota: {min(notas)}")
    
    print("Notas em ordem decrescente:")

    notas.sort(reverse=True)

    for nota in notas:
        print(nota)
else:
    print("Nenhuma nota cadastrada.")
