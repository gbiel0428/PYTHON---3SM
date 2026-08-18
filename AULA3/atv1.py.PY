import os
os.system("cls")

A = int(input("Informe o Número A: "))
B = int(input("Informe o Número B: "))

print("\n")

if (A > B):
    print("A e maior que B.")
elif (B > A):
    print("B é Maior que A.")
else:
    print("Números iguais.")