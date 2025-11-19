

try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    num3 = float(input("Introduce el tercer número: "))

    if num1 == num2 and num2 == num3:
        print("Los tres números son iguales.")
    elif num1 == num2:
        print("El primer y segundo número son iguales.")
    elif num1 == num3:
        print("El primer y tercer número son iguales.")
    elif num2 == num3:
        print("El segundo y tercer número son iguales.")

    mayor = max(num1, num2, num3)
    menor = min(num1, num2, num3)

    print(f"El número mayor es: {mayor}")
    print(f"El número menor es: {menor}")

except ValueError:
    print("Error: Por favor, introduce números válidos.")