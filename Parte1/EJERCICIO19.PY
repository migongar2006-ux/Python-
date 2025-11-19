

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3

if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <= num3:
    menor = num2
else:
    menor = num3

print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")

if num1 == num2 and num2 == num3:
    print("Los tres números son iguales.")
elif num1 == num2:
    print("El primero y el segundo son iguales.")
elif num1 == num3:
    print("El primero y el tercero son iguales.")
elif num2 == num3:
    print("El segundo y el tercero son iguales.")
else:
    print("No hay números iguales entre sí (son todos distintos).")