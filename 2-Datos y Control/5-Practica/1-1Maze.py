#Este es el de Nate

import os
import readchar

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15

my_position = [3, 1]

my_position[POS_X]
my_position[POS_Y]



while True: 
    #Draw Map
    print('+' + '-' * MAP_WIDTH * 3 + '+')
    for coordinate_y in range(MAP_HEIGHT):
        print('|', end ='')
        for coordinate_x in range(MAP_WIDTH):
            if coordinate_x == my_position[POS_X] and coordinate_y == my_position[POS_Y]:
                print(" @ ", end='')
            else:
                print('   ', end='')
        print('|')

    print('+' + '-' * MAP_WIDTH * 3 + '+')


    #Ask user ehere he wants to move

    #direction = input('Donde te queres mover? [WASD]: ')
    direction = readchar.readchar()

    if direction == 'w':
        my_position[POS_Y] -=1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == 's':
        my_position[POS_Y] +=1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == 'a':
        my_position[POS_X] -=1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == 'd':
        my_position[POS_X] +=1
        my_position[POS_X] %= MAP_WIDTH

    os.system('cls')

    