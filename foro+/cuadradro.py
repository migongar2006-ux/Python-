try:
    n = int(input("Introduce el tamaño del cuadrado (Recomendado n > 7): "))
except ValueError:
    print("Por favor, introduce un número entero.")
    exit()

# Definimos los límites del cuadro interno
# Usamos n//4 para que quede proporcionalmente en el centro
margen = n // 4
inicio_int = margen
fin_int = n - 1 - margen

print(f"\n--- Cuadrado Complejo (n={n}) ---\n")

for i in range(n):
    for j in range(n):
        
        # 1. Borde Exterior
        borde_ext = (i == 0 or i == n - 1 or j == 0 or j == n - 1)
        
        # 2. Diagonales
        diagonales = (i == j or i + j == n - 1)
        
        # 3. Cuadro Interno (Límites horizontales y verticales)
        # Estamos en la fila de inicio o fin, Y dentro del rango horizontal?
        filas_int = (i == inicio_int or i == fin_int) and (inicio_int <= j <= fin_int)
        # Estamos en la columna de inicio o fin, Y dentro del rango vertical?
        cols_int = (j == inicio_int or j == fin_int) and (inicio_int <= i <= fin_int)
        
        cuadro_interno = filas_int or cols_int
        
        # SI CUMPLE CUALQUIERA, PINTAMOS
        if borde_ext or diagonales or cuadro_interno:
            print("*", end=" ")
        else:
            print(" ", end=" ")
            
    print()