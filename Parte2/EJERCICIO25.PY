facultades = {
    "ingenieria": {"importe": 300, "mensualidad": 650},
    "derecho": {"importe": 250, "mensualidad": 550},
    "medicina": {"importe": 400, "mensualidad": 800},
    "educacion": {"importe": 200, "mensualidad": 450}
}

nombre_postulante = input("Introduce el nombre del postulante: ")
print("Facultades disponibles: Ingenieria, Derecho, Medicina, Educacion")
facultad_elegida = input("Introduce la facultad a estudiar: ").lower()

if facultad_elegida in facultades:
    costes = facultades[facultad_elegida]
    importe = costes["importe"]
    mensualidad = costes["mensualidad"]
    
    base_igv = importe + mensualidad
    igv = base_igv * 0.18
    monto_final = base_igv + igv

    print("\n--- Resumen de Matrícula ---")
    print(f"Postulante: {nombre_postulante}")
    print(f"Facultad: {facultad_elegida.capitalize()}")
    print(f"Importe de matrícula: {importe:.2f}")
    print(f"Mensualidad: {mensualidad:.2f}")
    print(f"IGV (18%): {igv:.2f}")
    print(f"Monto final a pagar: {monto_final:.2f}")
else:
    print("Error: La facultad introducida no es válida.")