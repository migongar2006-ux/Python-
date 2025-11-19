

USUARIO_CORRECTO = "admin"
CONTRASENA_CORRECTA = "12345"

usuario = input("Nombre de usuario: ")
contrasena = input("Contraseña: ")

if usuario == USUARIO_CORRECTO and contrasena == CONTRASENA_CORRECTA:
    print("Inicio de sesión correcto.")
elif usuario != USUARIO_CORRECTO:
    print("Nombre de usuario incorrecto.")
else:
    print("Contraseña incorrecta.")