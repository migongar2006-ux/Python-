

try:
    precio_original = float(input("Introduce el precio original del artículo: "))
    precio_venta = float(input("Introduce el precio de venta real: "))

    if precio_original > 0 and precio_venta >= 0:
        descuento_realizado = precio_original - precio_venta
        porcentaje_descuento = (descuento_realizado / precio_original) * 100
        print(f"\nEl porcentaje de descuento realizado es del {porcentaje_descuento:.2f}%")
    else:
        print("Error: Los precios no pueden ser negativos.")

except ValueError:
    print("Error: Por favor, introduce números válidos.")