import random
print("Adivina el numero")

numero_secreto = random.randint(1, 10)
intento = int(input("Escribe un numero del 1 al 10: "))

if intento == numero_secreto:
    print("Felicidades, adivinasste el numero")
else:
    print("No adivinaste. El numero era", numero_secreto)