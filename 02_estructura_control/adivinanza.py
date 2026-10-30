# ahora, haremos un juego de adivinanza, el usuario adivinara el numero mientras nosotros le damos pistas con un bucle while

import random # La libreria para escoger numeros aleatorios
num_aleatorio = random.randint(1, 20) # escoge un numero entre 1 y 20 al azar

numero = int(input("adivina el numero secreto: "))

while numero != num_aleatorio:
    if numero > num_aleatorio:
        print("tu numero es mayor, intenta nuevamente")
    elif numero < num_aleatorio:
        print("tu numero es menor, intenta nuevamente")
        
    numero = int(input("adivina el numero secreto: "))
        

print("Felicidades! Haz adivinado el numero")
    