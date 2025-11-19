

try:
    monto_compra = float(input("Introduce el monto de la compra: "))
    dia_semana = input("Introduce el día de la semana: ").lower()

    descuento = 0
    if dia_semana == "martes" or dia_semana == "jueves":
        descuento = monto_compra * 0.15
        print(f"\n¡Día de descuento! Se aplica un 15%.")
    
    total_pagar = monto_compra - descuento

    print(f"Descuento aplicado: {descuento:.2f}")
    print(f"Total a pagar: {total_pagar:.2f}")

except ValueError:
    print("Error: Introduce un monto de compra numérico válido.")