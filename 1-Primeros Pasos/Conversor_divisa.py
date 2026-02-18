#Esta es la mejora de la "Tarea 2" del "Primer programa"

dolar_euro = 0.91
libra_euro = 1.18

opcion = input('Cual es la clase de conversion que estas buscando?\n'
                'A - Dolar a Euro\n'
                'B - Euro a Dolar\n'
                'C - Libra a Euro\n'
                'D - Euro a Libra\n'
                'Tu respuesta: ')

texto_usuario = 'Introduzca la cantidad de {} a convertir: $'

if opcion == "A":
    cantidad_de_dinero = float(input(texto_usuario.format('Dolares')))
    print('La cantidad en Euros es: {}'.format(cantidad_de_dinero * dolar_euro))

elif opcion =="B":
    cantidad_de_dinero = float(input(texto_usuario.format('Euros')))
    print('La cantidad en Dolares es: {}'.format(cantidad_de_dinero / dolar_euro))

elif opcion == "C":
    cantidad_de_dinero = float(input(texto_usuario.format('Libras')))
    print('La cantidad en Euros es: {}'.format(cantidad_de_dinero * libra_euro))

elif opcion == "D":
    cantidad_de_dinero = float(input(texto_usuario.format('Euros')))
    print('La cantidad en Libras es: {}'.format(cantidad_de_dinero / libra_euro))

else:
    print('No has elegido ninguna opcion valida')