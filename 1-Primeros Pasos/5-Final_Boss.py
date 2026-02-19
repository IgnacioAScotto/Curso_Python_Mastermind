print('El camino a la gloria sudamericana\n'
      '----------------------------------\n'
      'Supongamos que sos el DT de river plate en esta temporada 2026, y tu objetivo es ganar la Copa Sudamericana\n'
      'teniendo en cuenta el estado actual del club luego de 5 fechas de campeonato y con chance de comprar jugadores\n'
      'vas a tener que tomar algunas decisiones que te pueden llevar a la gloria sudamericana\n'
      'o a tu despido...\n'
      '\n'
      'Teniendo en cuenta que los jugadores de River no hacen gol hace varios partidos. Traes un 9?\n')

import random
oferta_9 = random.randint(1,10)

opcion = input('[OPCION (A) - Si] | [OPCION (B) - No, y juego con los mismos] | [OPCION (C) - No, y pongo a los pibes] : ')

if opcion == "A":
    print('Tenes que ofertar por Luciano Gondou\n'  
          'Tenes que hacer la cuenta de cuantos millones debes poner por el delantero, si le erras no van a aceptar la oferta.\n'
          'La cuenta es 10*{}'.format(oferta_9))
    opcion = int(input('Cual es el resultado?: '))
    if opcion == 10 * oferta_9:
        print('Correcto, contrataste al 9, y esto te lleva a las semis contra Racing donde ganas con su Gol.')
    else:
        print('Incorrecto, no podes cerrar al 9 y quedas afuera en fase de grupos\n'
              'Estas DESPEDIDO')
        exit()
elif opcion == "B":
    print('Quedas afuera en 16vos de final\n'
          'Estas DESPEDIDO')
    exit()
elif opcion == "C":
    print('Poner fe en los pibes hace que llegues a 8vos de Final\n'
          'Pero llego el mercado de invierno y te falta jerarquia, ahora si traes un 9?')
    opcion = input('[OPCION (A) - Si] | [OPCION (B) - No]: ')
    if opcion == "A":
        print('Traes a Lunciano Gondou y te lleva a la Final contra el Santos de Neymar')
    elif opcion == "B":
        print('Te termino faltando jerarquia y quedas afuera en semis contra el Racing de Costas\n'
              'Estas DESPEDIDO')
        exit()
    else:
        print('No estas haciendo nada por el club\n'
          'Estas DESPEDIDO')
        exit()
else:
    print('No estas haciendo nada por el club\n'
          'Estas DESPEDIDO')
    exit()

consejo_de_hincha_tomado = False

print('De camino al estadio escuchas que un Hincha te dice que deberias poner a Rivero y no ha Paulo diaz, que haces?')

opcion = input('[Opcion (A) - Tomas el consejo] | [Opcion (B) - Ignoras el consejo]: ')

if opcion =="A":
    print('Decidiste escuchar el consejo dell hincha y te va a ayudar para mas adelante')
    consejo_de_hincha_tomado = True
elif opcion == "B":
    print('Estas seguro de que vos sabes mucho mas de futbol que el hincha y lo ignoras')
else:
    print('No estas haciendo nada por el club\n'
          'Estas DESPEDIDO')
    exit()
    
print('Ya estas en la final, tenes que tomar una decision importante:\n'
      'Pones al pibe Beltran que es el que viene atajando en la Liga, o pones la jerarquia de Armani para un Last Dance que es el que viene atajando tanto en Copa Sudamericana como en Copa Argnetina?')

opcion = input('[Opcion (A) - Beltran] | [Opcion (B) - Armani]: ')

if opcion == "A" and consejo_de_hincha_tomado == False:
    print('Lamentablemente el pibe no puede atajar un mano a mano despues de un error de Paulo Diaz en el minuto 88 y perdes la final en el alargue\n'
          'Estas DESPEDIDO')
    exit()
elif opcion == "A" and consejo_de_hincha_tomado == True:
    print('Lamentablemente el pibe no puede atajar un mano a mano en el minuto 88 PERO APARECE RIVERO Y LA SACA EN LA LINEA\n'
          'Y en el contraataque Luciano Gondou la manda al fondo de la red')
elif opcion == "B":
    print('Armani salva un mano a mano en el minuto 88 y Luciano Gondou mete el gol de la victoria en la contra')
else:
    print('No estas haciendo nada por el club\n'
          'Estas DESPEDIDO')
    exit()

print('Felicitaciones, sos CAMPEON de la COPA SUDAMERICANA\n'
      'Ahora Vamos por la LIBERTADORES')