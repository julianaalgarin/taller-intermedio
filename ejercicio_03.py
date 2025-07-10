# Contador de vocales
# Solicita al usuario una palabra y, con un for,
# cuenta cuántas vocales (a, e, i, o, u) contiene. Muestra el total al final.

palabra = input("Escriba una palabra: ")
vocales = "aeiou"

contador = 0

for Letra in palabra:
    if Letra.lower() in vocales:
        contador +=1

print (f"la palabra {palabra} tiene {contador} vocales")        
