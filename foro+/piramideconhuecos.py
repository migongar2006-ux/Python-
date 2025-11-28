try:
    altura = int(input("Introduce la altura de la pirámide: "))
except ValueError:
    exit()

print()
for i in range(altura):
    # Espacios alineación + Bloque repetido
    print(" " * (altura - 1 - i) + "* " * (i + 1))