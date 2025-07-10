# Suma hasta cero
# Crea un programa que lea números del usuario repetidamente con while hasta que ingrese un 0. Al finalizar,
# muestra la suma de todos los valores ingresados (excluyendo el cero).

suma = 0
numero = int (input("ingresa un número (0 para terminar): "))

while numero != 0:
      suma += numero
      numero = int (input("ingresa un número (0 para terminar): "))
      


print(f"La suma total fue {suma}") 