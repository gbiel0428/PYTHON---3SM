import os
os.system("cls")


while True:
    
        try:
            n1 = int(input("Informe Um Número Pra Tabuada: "))
            for i in range(1 , 11):
                print(f"{n1} x {i} = {n1 * i}")
            break
        except ValueError:
                print("Informe Apenas Números Inteiros.")
            
