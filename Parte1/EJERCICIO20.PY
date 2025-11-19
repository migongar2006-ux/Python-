
n = int(input("Introduce un número N (positivo): "))

if n < 0:
    print("Error: El número debe ser positivo.")
else:
    if n == 0:
        factorial = 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial = factorial * i
    
    print(f"El factorial de {n}! es: {factorial}")