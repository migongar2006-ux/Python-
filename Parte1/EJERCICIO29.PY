

print("Piensa un número del 1 al 100.")
print("Yo intentaré adivinarlo.")
print("Respóndeme con 'mayor', 'menor' o 'igual'.")

limite_inferior = 1
limite_superior = 100
intentos = 0

while True:
    intentos += 1
    
    propuesta = (limite_inferior + limite_superior) // 2
    
    respuesta = input(f"¿Es tu número el {propuesta}? (mayor/menor/igual): ").lower()
    
    if respuesta == "igual":
        print(f"¡Genial! He adivinado tu número ({propuesta}) en {intentos} intentos.")
        break
    elif respuesta == "mayor":
        
        limite_inferior = propuesta + 1
    elif respuesta == "menor":
       
        limite_superior = propuesta - 1
    else:
        print("Respuesta no válida. Por favor, escribe 'mayor', 'menor' o 'igual'.")

    if limite_inferior > limite_superior:
        print("¡Has hecho trampa! No hay números que cumplan esas condiciones.")
        break