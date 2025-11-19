

import math

try:
    radio = float(input("Introduce la longitud del radio: "))

    if radio >= 0:
        diametro = 2 * radio
        longitud_circunferencia = math.pi * diametro
        area_circulo = math.pi * (radio ** 2)
        volumen_esfera = (4/3) * math.pi * (radio ** 3)

        print(f"\nPara un radio de {radio}:")
        print(f"La longitud de la circunferencia es: {longitud_circunferencia:.2f}")
        print(f"El área del círculo es: {area_circulo:.2f}")
        print(f"El volumen de la esfera es: {volumen_esfera:.2f}")
    else:
        print("Error: El radio no puede ser un número negativo.")

except ValueError:
    print("Error: Por favor, introduce un número válido para el radio.")