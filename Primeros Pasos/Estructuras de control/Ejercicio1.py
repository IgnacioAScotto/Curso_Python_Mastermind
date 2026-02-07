# Adivina el numero:
#Crea un programa en el cual el usuario tenga que adivinar un numero del 1 al 10. Cuando se pregunte al usuario cual es el numero que esta dentro de la secuencia,
#en el caso de que acierte se debe felicitarlo por adivinar, sino se termina el juego.

print('BIENVENIDO AL ADIVINADOR')
numero = 4
numero_de_jugador = int(input('Ingresa el numero del 1 al 10 que crees que es: '))

if numero_de_jugador == numero:
    print('Adivinaste, felicitaciones')



#Ejercicio pero con numeros random y que no se pueda elegir otro numero

import random

print('BIENVENIDO AL ADIVINADOR')
numero = random.randint(1, 10)
numero_de_jugador = int(input('Ingresa el numero del 1 al 10 que crees que es: '))

if numero_de_jugador >10:
    print('Te pasate, el maximo es 10')

if numero_de_jugador <1:
    print('Te quedaste corto')

if numero_de_jugador == numero:
    print('Adivinaste, felicitaciones')

print(f'El numero ganador era {numero}')
