try:
    n = int(input("Introduce la altura del triángulo invertido: "))
except ValueError:
    print("Introduce un número entero.")
    exit()

print(f"\n--- Triángulo Alternado (n={n}) ---\n")

for i in range(n):
    # Calcular espacios a la izquierda (sangría)
    espacios_izq = " " * i
    
    # Lógica de dibujo por fila
    if i == 0:
        # Fila superior: Todo asteriscos
        print("*" * (2 * n - 1))
        
    elif i == n - 1:
        # La punta: Solo un asterisco
        print(espacios_izq + "*")
        
    else:
        # Filas intermedias (Borde + Relleno + Borde)
        ancho_hueco = 2 * (n - i) - 3
        
        # EL TRUCO: Alternar relleno según si la fila es par o impar
        if i % 2 == 0:
            relleno = "*" * ancho_hueco # Fila par: Rellena
        else:
            relleno = " " * ancho_hueco # Fila impar: Vacía
            
        print(espacios_izq + "*" + relleno + "*")