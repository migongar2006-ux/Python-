

nombre_trabajador = input("Introduce el nombre del trabajador: ")
try:
    horas_trabajadas = float(input("Introduce el número de horas trabajadas en la semana: "))
    tarifa_normal = float(input("Introduce la tarifa por hora normal (€): "))

    if horas_trabajadas <= 35:
        salario_bruto = horas_trabajadas * tarifa_normal
    else:
        horas_normales = 35
        horas_extra = horas_trabajadas - 35
        salario_bruto = (horas_normales * tarifa_normal) + (horas_extra * tarifa_normal * 1.5)

    impuestos = 0
    if salario_bruto > 500:
        if salario_bruto <= 900: 
            impuestos = (salario_bruto - 500) * 0.25
        else: 
            impuestos = (400 * 0.25) + ((salario_bruto - 900) * 0.45)

    salario_neto = salario_bruto - impuestos

    print("\n--- Resumen de Salario ---")
    print(f"Trabajador: {nombre_trabajador}")
    print(f"Salario Bruto: {salario_bruto:.2f} €")
    print(f"Tasas (impuestos): {impuestos:.2f} €")
    print(f"Salario Neto Semanal: {salario_neto:.2f} €")

except ValueError:
    print("Error: Introduce valores numéricos válidos para las horas y la tarifa.")