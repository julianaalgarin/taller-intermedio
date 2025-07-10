# Lista de cuadrados
# Genera una lista que contenga los cuadrados de los números del 1 al 10
# usando un for, y luego muestra la lista completa.


cuadrados = []

for i in range(1, 11):
    cuadrado = i ** 2
    cuadrados.append(cuadrado)

print(cuadrados)
