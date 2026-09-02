import os
os.system("cls")

notas = []

while True:
    try:
        for i in range(3):
            n1 = int(input(f"Informe a {i + 1}° Nota: "))
            notas.append(n1)
        media =sum(notas) / len(notas)
        if media >=7:
            print(f"Sua Media foi: {media:.2f}, Então Voce esta Aprovado. ")
        elif media >=5 and  media <=6.9:
            print(f"Sua Media foi: {media:.2f}, Então Voce esta Recuperação. ")
        else:
            print(f"Sua Media foi: {media:.2f}, Então Voce esta Reprovado. ")
        break
    except ValueError:
        print("Informe uma Nota Inteira.")