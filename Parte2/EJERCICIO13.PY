

try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    if num1 < num2:
        print(f"Los números en orden ascendente son: {num1}, {num2}")
    elif num2 < num1:
        print(f"Los números en orden ascendente son: {num2}, {num1}")
    else:
        print(f"Ambos números son iguales: {num1}")

except ValueError:
    print("Error: Por favor, introduce números válidos.")