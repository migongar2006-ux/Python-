
try:
    valor_compra = float(input("Introduce el valor de la compra: "))
    tipo_pago = input("Introduce el tipo de pago (contado / tarjeta): ").lower()

    descuento = 0
    recargo = 0

    if tipo_pago == "contado":
        descuento = valor_compra * 0.05
        total_pagar = valor_compra - descuento
        print(f"\nDescuento por pago al contado (5%): {descuento:.2f}")
        print(f"Total a pagar: {total_pagar:.2f}")
    elif tipo_pago == "tarjeta":
        recargo = valor_compra * 0.03
        total_pagar = valor_compra + recargo
        print(f"\nRecargo por pago con tarjeta (3%): {recargo:.2f}")
        print(f"Total a pagar: {total_pagar:.2f}")
    else:
        print("\nError: Tipo de pago no válido. Use 'contado' or 'tarjeta'.")
        print(f"Total a pagar (sin cambios): {valor_compra:.2f}")

except ValueError:
    print("Error: Introduce un valor de compra numérico válido.")