

try:
    edad = int(input("Introduce tu edad: "))
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
except ValueError:
    print("Error: Por favor, introduce un número entero válido para la edad.")