from random import randint

vida_pikachu = 80
vida_squirtle = 90

vida_inicial_pikachu = vida_pikachu
vida_inicial_squirtle = vida_squirtle


while vida_pikachu>0 and vida_squirtle>0:
    #se desenvuelven los turnos de combate

    #Turno de Pikachu
    print('Turno de Pikachu')
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        #Bola Voltio
        print('Pikachu ataca con Bola Voltio')
        vida_squirtle -= 10
    else:
        print('Pikachu ataca con Onda Trueno')
        vida_squirtle -= 11

    print('La vida de Pikachu es {}, la vida de Squirtle es {}'.format(vida_pikachu, vida_squirtle))

    porcentaje_vida_pikachu = vida_pikachu / vida_inicial_pikachu 
    porcentaje_vida_squirtle = vida_squirtle / vida_inicial_squirtle 

    cantidad_vida_pikachu = int(porcentaje_vida_pikachu * 10)
    cantidad_vida_squirtle = int(porcentaje_vida_squirtle * 10)

    vacios_pikachu = 10-cantidad_vida_pikachu
    vacios_squirtle = 10-cantidad_vida_squirtle

    print('[{}] - [{}]'.format('#' * cantidad_vida_pikachu + ' ' * vacios_pikachu, '#' * cantidad_vida_squirtle + ' ' * vacios_squirtle))

    input('Enter para Continuar...')

    #Turno Squirtle
    print('Turno Squirtle')
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

    print('La vida de Pikachu es {}, la vida de Squirtle es {}'.format(vida_pikachu, vida_squirtle))

    porcentaje_vida_pikachu = vida_pikachu / vida_inicial_pikachu 
    porcentaje_vida_squirtle = vida_squirtle / vida_inicial_squirtle 

    cantidad_vida_pikachu = int(porcentaje_vida_pikachu * 10)
    cantidad_vida_squirtle = int(porcentaje_vida_squirtle * 10)

    vacios_pikachu = 10-cantidad_vida_pikachu
    vacios_squirtle = 10-cantidad_vida_squirtle

    print('[{}] - [{}]'.format('#' * cantidad_vida_pikachu + ' ' * vacios_pikachu, '#' * cantidad_vida_squirtle + ' ' * vacios_squirtle))


if vida_pikachu > vida_squirtle:
    print('Gana Pikachu')
else:
    print('Squirtle Gana')