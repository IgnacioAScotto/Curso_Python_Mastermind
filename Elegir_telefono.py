# Hacer un programa que de las opciones de: Android o Iphone

telefono = input('Elegi que SO queres:\n'
                  'A - Android\n'
                  'B - IOS\n'
                  'Tu Respuesta: ')


if telefono == "A":
    dinero = input('Tienes dinero:\n'
                   'A - Si\n'
                   'B - No\n'
                   'Tu Respuesta: ')
    if dinero == 'A':
        camara = input('Te importa la camara del celular?\n'
                       'A - Si\n'
                       'B - No\n'
                       'Tu Respuesta: ')
        if camara == 'A':
            print('Comprate el Google Pixel Supercamara')
        elif camara == 'B':
            print('Comprate el Andorid calidad precio')
        else:
            print('La opcion que elegiste no es valida')
    else:
        print('Comprate el Android Chino de $100usd')
elif telefono == "B":
    dinero = input('Tienes dinero:\n'
                   'A - Si\n'
                   'B - No\n'
                   'Tu Respuesta: ')
    if dinero == 'A':
        print('Comprate el ultimo PRO MAX')
    elif dinero == 'B':
        print('Comprate un Iphone de segunda mano')
    else:
        print('La opcion que elegiste no es valida')
else:
    print('La opcion que elegiste no es valida')
    