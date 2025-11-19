

MILLA_MARINA_EN_METROS = 1852

try:
    millas_marinas = float(input("Introduce la distancia en millas marinas: "))

    if millas_marinas >= 0:
        metros = millas_marinas * MILLA_MARINA_EN_METROS
        print(f"{millas_marinas} millas marinas equivalen a {metros:.2f} metros.")
    else:
        print("Error: La distancia no puede ser negativa.")

except ValueError:
    print("Error: Por favor, introduce un número válido.")