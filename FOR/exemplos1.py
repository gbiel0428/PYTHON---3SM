import os
os.system("cls")

temperatura = []

for i in range(5):
    temp = float(input(f"Informe a {i+1}ª Temperatura: "))
    temperatura.append(temp)
    
media = sum(temperatura) / len(temperatura)

menor = min(temperatura)
maior = max(temperatura)

print(f"As Temperaturas são: {temperatura}")
print(f"A Media das Temperatura é: {media}")
print(f"A Menor Temperatura é: {menor} °C")
print(f"A Maior Temperatura é: {maior} °C")