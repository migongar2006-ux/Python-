
try:
    h = int(input("Introduce la hora (0-23): "))
    m = int(input("Introduce los minutos (0-59): "))
    s = int(input("Introduce los segundos (0-59): "))

    if not (0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59):
        print("Error: Los valores introducidos no forman una hora válida.")
    else:
        s += 1

        if s == 60:
            s = 0
            m += 1
        
        if m == 60:
            m = 0
            h += 1
        
        if h == 24:
            h = 0

        print(f"Un segundo después, la hora será: {h:02d}:{m:02d}:{s:02d}")

except ValueError:
    print("Error: Introduce valores enteros válidos para la hora.")