def estrella_ocho_puntas(n):
    if n % 2 == 0:
        print("Por favor, usa un número impar para tener un centro exacto.")
        return

    centro = n // 2 # División entera

    for i in range(n):
        for j in range(n):
            # Condición 1: Diagonal principal (i == j)
            # Condición 2: Diagonal inversa (i + j == n - 1)
            # Condición 3: Línea horizontal (i == centro)
            # Condición 4: Línea vertical (j == centro)
            
            if (i == j) or (i + j == n - 1) or (i == centro) or (j == centro):
                print("*", end=" ") # Agrego un espacio extra para que se vea menos 'aplastado'
            else:
                print(" ", end=" ")
        
        print() # Salto de línea al terminar la fila

# Probamos con n=9
imput_n = int(input("Ingrese un número impar para la estrella de ocho puntas: "))
estrella_ocho_puntas(imput_n)