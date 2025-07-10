# Pares e impares
# Dada la lista [3, 8, 15, 22, 7, 10, 13], recórrela con un for y utiliza
# dos contadores para determinar cuántos son
# pares y cuántos impares. Muestra ambos totales.

lista = [3, 8, 15, 22, 7, 10, 13]
pares = 0
impares = 0

for numero in lista:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Pares: {pares}")
print(f"Impares: {impares}")

