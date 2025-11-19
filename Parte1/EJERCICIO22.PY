
cont_positivos = 0
cont_negativos = 0

print("Introduce 100 números (distintos de cero):")

for i in range(100):
    numero = float(input(f"Número {i + 1}/100: "))
    
    if numero > 0:
        cont_positivos += 1
    elif numero < 0:
        cont_negativos += 1

print(f"Total de números positivos: {cont_positivos}")
print(f"Total de números negativos: {cont_negativos}")