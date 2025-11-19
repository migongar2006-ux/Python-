
suma_pares = 0
suma_impares = 0

for numero in range(100, 201):
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero

print(f"La suma de los números PARES entre 100 y 200 es: {suma_pares}")
print(f"La suma de los números IMPARES entre 100 y 200 es: {suma_impares}")