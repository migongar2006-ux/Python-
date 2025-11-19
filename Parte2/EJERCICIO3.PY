

try:
    lado = float(input("Introduce la longitud del lado del cuadrado: "))
    area = lado * lado
    print(f"El área del cuadrado es: {area}")
except ValueError:
    print("Error: Por favor, introduce un número válido.")