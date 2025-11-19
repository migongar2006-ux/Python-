
try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    suma = num1 + num2
    resta = num1 - num2
    producto = num1 * num2
    
    division = num1 / num2

    print(f"\nResultados para {num1} y {num2}:")
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Producto: {producto}")
    print(f"División: {division}")

except ValueError:
    print("Error: Por favor, introduce números válidos.")