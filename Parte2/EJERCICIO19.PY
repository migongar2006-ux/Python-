

saldo = 1000.0

while True:
    print("\nBienvenido a su Cajero Virtual")
    print("---------------------------------")
    print("Saldo actual: ${:.2f}".format(saldo))
    print("1. Ingresar dinero en cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Salir")
    
    opcion = input("Seleccione una opción (1-3): ")

    if opcion == '1':
        try:
            ingreso = float(input("Cantidad a ingresar: "))
            if ingreso > 0:
                saldo += ingreso
                print(f"Ingreso realizado con éxito. Nuevo saldo: ${saldo:.2f}")
            else:
                print("La cantidad a ingresar debe ser positiva.")
        except ValueError:
            print("Error: Cantidad no válida.")
    
    elif opcion == '2':
        try:
            retiro = float(input("Cantidad a retirar: "))
            if retiro <= 0:
                print("La cantidad a retirar debe ser positiva.")
            elif retiro > saldo:
                print("Saldo insuficiente.")
            else:
                saldo -= retiro
                print(f"Retiro realizado con éxito. Nuevo saldo: ${saldo:.2f}")
        except ValueError:
            print("Error: Cantidad no válida.")

    elif opcion == '3':
        print("Gracias por utilizar nuestro cajero. ¡Hasta pronto!")
        break
    
    else:
        print("Opción no válida. Por favor, elija una opción del 1 al 3.")