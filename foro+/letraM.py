while True:
    try:
        n = int(input("Introduce la altura de la M (Impar, ej: 7): "))
        if n % 2 != 0:
            break
        print("Por favor, usa un número impar para que las diagonales se encuentren justo en el centro.")
    except ValueError:
        print("Introduce un número entero.")

centro = n // 2
print(f"\n--- Letra M (n={n}) ---\n")

for i in range(n):
    for j in range(n):
        # 1. Columnas verticales (siempre se pintan)
        condicion_columnas = (j == 0 or j == n - 1)
        
        # 2. Diagonales (SOLO si estamos en la mitad superior o el centro)
        condicion_diagonales = (i == j or i + j == n - 1) and (i <= centro)
        
        if condicion_columnas or condicion_diagonales:
            print("*", end=" ")
        else:
            print(" ", end=" ")
            
    print()