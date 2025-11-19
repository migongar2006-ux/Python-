cont_positivos = 0
cont_negativos = 0
ha_leido_negativo = False

print("Introduce números (introduce 0 para terminar):")

while True:
    numero = float(input("Introduce un número: "))
    
    if numero == 0:
        break  
    
    if numero > 0:
        cont_positivos += 1
    else: 
        cont_negativos += 1
        ha_leido_negativo = True
print("\n--- Resultados ---")
if ha_leido_negativo:
    print("Se ha leído al menos un número negativo.")
else:
    print("No se han leído números negativos.")

print(f"Cantidad de números positivos: {cont_positivos}")
print(f"Cantidad de números negativos: {cont_negativos}")