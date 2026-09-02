import os
os.system("cls")

negativos = [ ]
positivos =  [ ]

for i in range(10):
    num = int(input("Informe os Números: "))
    if (num>=0):
        positivos.append(num)
    else:
        negativos.append(num)
print(f"Números Negativos: {negativos}")
print(f"Números Positivos: {positivos}")
print(f"A soma dos positivos: {sum(positivos)}")