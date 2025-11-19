

try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    suma = num1 + num2
    resta = num1 - num2
    producto = num1 * num2

    print(f"\nResultados para {num1} y {num2}:")
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Producto: {producto}")

    if num2 != 0:
        division = num1 / num2
        print(f"División: {division}")
    else:
        print("División: No es posible dividir por cero.")

except ValueError:
    print("Error: Por favor, introduce números válidos.")