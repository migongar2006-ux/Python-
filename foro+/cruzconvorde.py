while True:
    try:
        n = int(input("Introduce el tamaño de la cuadrícula (IMPAR, ej: 7): "))
        if n % 2 != 0:
            break
        print("Para que la cruz quede centrada, el número debe ser impar.")
    except ValueError:
        print("Por favor, introduce un número entero.")

centro = n // 2

print(f"\n--- Cruz con borde para n={n} ---\n")

for i in range(n):
    for j in range(n):
        # 1. Prioridad: La Cruz
        if i == centro or j == centro:
            print("*", end=" ")
        
        # 2. Prioridad: El Borde (Solo si no es cruz)
        elif i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print(".", end=" ")
            
        # 3. Resto: Relleno vacío
        else:
            print(" ", end=" ") # Espacio vacío
            
    print()