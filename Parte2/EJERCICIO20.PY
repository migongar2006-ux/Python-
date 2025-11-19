

try:
    nota = float(input("Introduce la calificación numérica (0-10): "))

    if not (0 <= nota <= 10):
        print("Error: La calificación debe estar entre 0 y 10.")
    elif nota < 3:
        print("Calificación: Muy Deficiente.")
    elif nota < 5:
        print("Calificación: Insuficiente.")
    elif nota < 6:
        print("Calificación: Suficiente.")
    elif nota < 7:
        print("Calificación: Bien.")
    elif nota < 9:
        print("Calificación: Notable.")
    else: # nota <= 10
        print("Calificación: Sobresaliente.")

except ValueError:
    print("Error: Introduce una calificación numérica válida.")