

try:
    numero = int(input("Introduce un número entero: "))

    if numero % 10 == 0:
        print(f"El número {numero} es múltiplo de 10.")
    else:
        print(f"El número {numero} no es múltiplo de 10.")

except ValueError:
    print("Error: Por favor, introduce un número entero válido.")