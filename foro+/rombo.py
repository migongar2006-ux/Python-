try:
    n = int(input("Introduce el tamaño del radio del rombo (n): "))
except ValueError:
    print("Por favor, introduce un número entero.")
    exit()

print(f"\n--- Rombo Sólido (n={n}) ---\n")

# --- PARTE SUPERIOR (Incluye la fila central) ---
for i in range(n):
    espacios = " " * (n - 1 - i)
    estrellas = "*" * (2 * i + 1)
    print(espacios + estrellas)

# --- PARTE INFERIOR (Espejo) ---
# Empezamos en n-2 para no repetir la fila del medio
for i in range(n - 2, -1, -1):
    espacios = " " * (n - 1 - i)
    estrellas = "*" * (2 * i + 1)
    print(espacios + estrellas)