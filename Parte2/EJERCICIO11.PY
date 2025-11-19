

try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    if num1 > num2:
        print(f"El número mayor es: {num1}")
    elif num2 > num1:
        print(f"El número mayor es: {num2}")
    else:
        print("Ambos números son iguales.")

except ValueError:
    print("Error: Por favor, introduce números válidos.")