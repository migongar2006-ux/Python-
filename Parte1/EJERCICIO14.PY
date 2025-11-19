num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

suma = num1 + num2
resta = num1 - num2
producto = num1 * num2

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Producto: {producto}")

if num2 == 0:
    print("División: No es posible dividir por cero.")
else:
    division = num1 / num2
    print(f"División: {division}")
