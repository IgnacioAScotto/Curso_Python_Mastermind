from random import randint

vida_pikachu = 80
vida_squirtle = 90

VIDA_INICIAL_PIKACHU = vida_pikachu
VIDA_INICIAL_SQUIRTLE = vida_squirtle

TAMANO_BARA_VIDA = 20


while vida_pikachu>0 and vida_squirtle>0:
    #se desenvuelven los turnos de combate

    #Turno de Pikachu
    print('\nTurno de Pikachu')
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        #Bola Voltio
        print('Pikachu ataca con Bola Voltio')
        vida_squirtle -= 10
    else:
        print('Pikachu ataca con Onda Trueno')
        vida_squirtle -= 11

    #Mostramos la vida de cada Pokemon

    barras_de_vida_pikachu = int(vida_pikachu * TAMANO_BARA_VIDA / VIDA_INICIAL_PIKACHU)
    print('Pikachu:    [{}{}] ({}/{})'.format('*' * barras_de_vida_pikachu, ' ' * (TAMANO_BARA_VIDA - barras_de_vida_pikachu), vida_pikachu, VIDA_INICIAL_PIKACHU))

    barras_de_vida_squirtle = int(vida_pikachu * TAMANO_BARA_VIDA / VIDA_INICIAL_SQUIRTLE)
    print('Squirtle:    [{}{}] ({}/{})'.format('*' * barras_de_vida_squirtle, ' ' * (TAMANO_BARA_VIDA - barras_de_vida_squirtle), vida_squirtle, VIDA_INICIAL_SQUIRTLE))

    input('Enter para Continuar...')

    #Turno Squirtle
    print('\nTurno Squirtle')
    ataque_squirtle = None
    while ataque_squirtle != "A" and ataque_squirtle != "B" and ataque_squirtle != "C":
        ataque_squirtle = input('Que ataque deseas realizar? [A]Placaje - [B]Burbuja - [C]Pistola Agua : ')
    
    if ataque_squirtle == "A":
        print('Squirtle ataca con Placaje')
        vida_pikachu -= 10
    elif ataque_squirtle == "B":
        print('Squirtle ataca con Burbuja')
        vida_pikachu -= 17
    else:
        print('Squirtle ataca con Pistola Agua')
        vida_pikachu -= 9

    #Mostramos la vida de cada Pokemon

    barras_de_vida_pikachu = int(vida_pikachu * TAMANO_BARA_VIDA / VIDA_INICIAL_PIKACHU)
    print('Pikachu:    [{}{}] ({}/{})'.format('*' * barras_de_vida_pikachu, ' ' * (TAMANO_BARA_VIDA - barras_de_vida_pikachu), vida_pikachu, VIDA_INICIAL_PIKACHU))

    barras_de_vida_squirtle = int(vida_pikachu * TAMANO_BARA_VIDA / VIDA_INICIAL_SQUIRTLE)
    print('Squirtle:    [{}{}] ({}/{})'.format('*' * barras_de_vida_squirtle, ' ' * (TAMANO_BARA_VIDA - barras_de_vida_squirtle), vida_squirtle, VIDA_INICIAL_SQUIRTLE)) 

    input('Enter para Continuar...')



if vida_pikachu > vida_squirtle:
    print('Gana Pikachu')
else:
    print('Squirtle Gana')