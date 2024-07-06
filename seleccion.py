from random import randint

numero = randint(1, 100)
print(numero)
intentos = 0

while intentos < 3:

    intentos += 1
    minumero = int(input(f"Que numero estoy pensando es entre 1 y 100 este es tu intento {intentos} de 3: "))

    if numero > minumero:
        print("Es Mayor")
    elif numero < minumero:
        print("Es Menor")
    else:
        print("Adivinaste")
        break

