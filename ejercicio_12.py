# Validación de contraseña
# Implementa un programa que solicite una contraseña correcta (puedes fijarla en tu código)
# y permita hasta 3 intentos.

# Si el usuario acierta: imprime “¡Acceso concedido!” y termina.

# Si agota los 3 intentos: imprime “Usuario bloqueado” y termina.



contraseña_correcta = "happierbyoliviarodrigo"
intentos = 0
acceso = False

while intentos < 3:
     ingreso = input ("Ingrese la contraseña: ")
     if ingreso == contraseña_correcta:
         acceso = True
         break
     intentos += 1
     print(f"Contraseña incorrecta. Intentos restantes: {3- intentos}")
if acceso:
     print("Bienvenido")
else:
     print("Demasiados intentos incorrectos")        
