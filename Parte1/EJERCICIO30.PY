
cantidad = int(input("Introduce una cantidad de Euros (múltiplo de 5): "))


if cantidad % 5 != 0:
    print("Error: La cantidad debe ser un múltiplo de 5.")
else:
    print(f"Para {cantidad} €, se necesita el mínimo de billetes:")
    
    
    billetes = [500, 200, 100, 50, 20, 10, 5]
    
    
    restante = cantidad
    
    for billete in billetes:
       
        numero_billetes = restante // billete
        
        if numero_billetes > 0:
            print(f"- {numero_billetes} billete(s) de {billete} €")
            
            
            restante = restante % billete 