
nombre = input("Introduce el nombre del trabajador: ")
tarifa_normal = float(input("Introduce la tarifa normal por hora (€): "))
horas_trabajadas = int(input("Introduce el número de horas trabajadas esta semana: "))

if horas_trabajadas <= 35:
    salario_bruto = horas_trabajadas * tarifa_normal
else:
    horas_normales = 35
    horas_extra = horas_trabajadas - 35
    salario_bruto = (horas_normales * tarifa_normal) + (horas_extra * (tarifa_normal * 1.5))


impuestos = 0
if salario_bruto > 900: 
    tramo_restante = salario_bruto - 900
    impuestos = (400 * 0.25) + (tramo_restante * 0.45)
elif salario_bruto > 500:
    tramo_25 = salario_bruto - 500
    impuestos = tramo_25 * 0.25
else:
    impuestos = 0


salario_neto = salario_bruto - impuestos


print("\n--- Recibo de Salario ---")
print(f"Trabajador: {nombre}")
print(f"Salario Bruto Semanal: {salario_bruto:.2f} €")
print(f"Total de Impuestos: {impuestos:.2f} €")
print(f"Salario Neto Semanal: {salario_neto:.2f} €")