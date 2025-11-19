precio_original = float(input("Introduce el precio original del artículo: "))
precio_venta = float(input("Introduce el precio de venta real: "))

descuento_realizado = precio_original - precio_venta
porcentaje_descuento = (descuento_realizado / precio_original) * 100

print(f"Se ha aplicado un descuento del: {porcentaje_descuento:.2f}%")