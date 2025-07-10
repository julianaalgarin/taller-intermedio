# Promedio de lista
# Dada la lista [12, 7, 22, 5, 14, 9], utiliza un for,
# un acumulador y un contador para calcular y mostrar su promedio.


lista = [12, 7, 22, 5, 14, 9]
suma = 0
contador = 0
for numero in lista:
    suma += numero
    contador +=1

promedio = suma / contador 
    
print(f"{promedio}")