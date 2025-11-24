def imprimir_diamante(n):
    # --- PARTE SUPERIOR (Incluye la fila del medio) ---
    for i in range(n):
        # 1. Espacios a la izquierda
        print(" " * (n - 1 - i), end="")
        
        # 2. Primer asterisco
        print("*", end="")
        
        # 3. Espacios internos y segundo asterisco (si no es la punta)
        if i > 0:
            print(" " * (2 * i - 1), end="")
            print("*", end="")
            
        print() # Salto de línea

    # --- PARTE INFERIOR (Espejo de la superior) ---
    # Vamos desde n-2 hasta 0 (hacia atrás)
    for i in range(n - 2, -1, -1):
        # 1. Espacios a la izquierda
        print(" " * (n - 1 - i), end="")
        
        # 2. Primer asterisco
        print("*", end="")
        
        # 3. Espacios internos y segundo asterisco
        if i > 0:
            print(" " * (2 * i - 1), end="")
            print("*", end="")
            
        print()

# Probamos con n=5
n = int(input("Ingrese la altura del diamante: "))
imprimir_diamante(n)