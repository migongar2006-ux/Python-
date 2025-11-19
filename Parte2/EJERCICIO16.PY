

try:
    numero_str = input("Introduce un número entre 0 y 99999: ")
    numero = int(numero_str)

    if 0 <= numero <= 99999:
        cifras = len(numero_str)
        print(f"El número {numero} tiene {cifras} cifra(s).")
    else:
        print("Error: El número está fuera del rango permitido (0-99999).")

except ValueError:
    print("Error: Por favor, introduce un número entero válido.")