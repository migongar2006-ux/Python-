import math
radio = float(input("Introduce la longitud del radio: "))

diametro = radio * 2
longitud_circunferencia = math.pi * diametro
area_circulo = math.pi * (radio ** 2)
volumen_esfera = (4/3) * math.pi * (radio ** 3)

print(f"Para un radio de {radio}:")
print(f"Longitud de la circunferencia: {longitud_circunferencia:.2f}")
print(f"Área del círculo: {area_circulo:.2f}")
print(f"Volumen de la esfera: {volumen_esfera:.2f}")