

try:
    numero = float(input("Introduce un número: "))

    if numero >= 0:
        print("El número es positivo.")
    else:
        print("El número es negativo.")

except ValueError:
    print("Error: Por favor, introduce un número válido.")