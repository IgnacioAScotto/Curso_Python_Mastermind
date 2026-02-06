# Adivina el numero:
#Crea un programa en el cual el usuario tenga que adivinar un numero del 1 al 10. Cuando se pregunte al usuario cual es el numero que esta dentro de la secuencia,
#en el caso de que acierte se debe felicitarlo por adivinar, sino se termina el juego.

print('BIENVENIDO AL ADIVINADOR')
numero = 4
numero_de_jugador = int(input('Ingresa el numero del 1 al 10 que crees que es: '))

if numero_de_jugador == numero:
    print('Adivinaste, felicitaciones')
