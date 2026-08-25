import os
os.system("cls")

numeros = [ ]


while True:
    amazenar = int(input("Informe o Número : "))
    if (amazenar!=0):
        numeros.append(amazenar)
    else:
        break
print(numeros)
soma = sum(numeros)
print(f"A soma dos numeros informados é: {soma}")