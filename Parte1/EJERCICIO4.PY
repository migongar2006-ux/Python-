num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

suma = num1 + num2
resta = num1 - num2
producto = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division = "Indefinida (no se puede dividir por cero)"

    print(f"Suma: {num1} + {num2} = {suma}")
print(f"Resta: {num1} - {num2} = {resta}")
print(f"Producto: {num1} * {num2} = {producto}")
print(f"División: {num1} / {num2} = {division}")