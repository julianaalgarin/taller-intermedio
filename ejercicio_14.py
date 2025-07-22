# Uso de break y continue
# Escribe un programa con while True que recorra números de 1 en adelante y:

# Use continue para saltar e imprimir solo los números que no sean múltiplos de 3.

# Detenga el bucle (break) cuando alcance el número 20.


num = 0

while True:
    num += 1

    if num == 20:
        break
    if num % 3 == 0:
        continue

    print(num)