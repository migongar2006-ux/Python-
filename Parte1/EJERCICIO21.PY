
ha_leido_negativo = False  

print("Introduce 100 números (distintos de cero):")

for i in range(100):
    numero = float(input(f"Número {i + 1}/100: "))
    
    
    if numero < 0:
        ha_leido_negativo = True
if ha_leido_negativo:
    print("Se ha introducido al menos un número negativo.")
else:
    print("No se han introducido números negativos.")