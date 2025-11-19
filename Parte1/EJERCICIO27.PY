
hubo_un_diez = False

print("Introduce notas (0-10). Escribe -1 para terminar.")

while True:
    nota = float(input("Nota: "))
    
    if nota == -1:
        break 
    
    if nota == 10:
        hubo_un_diez = True
    elif nota < 0 or nota > 10:
        print("Nota no válida (debe ser 0-10 o -1 para salir).")

if hubo_un_diez:
    print("Sí, se ha introducido al menos una nota con valor 10.")
else:
    print("No se ha introducido ninguna nota con valor 10.")