try:
    n = int(input("Introduce el tamaño del lado del cuadrado: "))
except ValueError:
    print("Debes introducir un número entero.")
    exit()

print(f"\n--- Cuadrado Mágico de lado {n} ---\n")

for i in range(n):
    for j in range(n):
        # Condición masiva: Borde Arriba/Abajo OR Borde Izq/Der OR Diagonales
        if (i == 0 or i == n - 1 or 
            j == 0 or j == n - 1 or 
            i == j or i + j == n - 1):
            
            print("*", end=" ") 
        else:
            print(" ", end=" ") # Espacio vacío (con el ajuste visual)
            
    print() # Salto de línea al terminar la fila