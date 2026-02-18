#se les da descuento a: -menores de 10, -universitarios entre 25 y 35, -mayores de 65 pensionistas, -familia numerosa

edad = int(input('Ingrese su edad: '))
tipo_de_carnet = input('Ingrese su tipo de carnet (E: Estudiante/ P: Pensionista/ F: Familia Numerosa/N: Nada): ')

if (25<=edad<=35 and tipo_de_carnet =='E') or edad<=10 or (edad>=65 and tipo_de_carnet == 'P') or (tipo_de_carnet == 'F'):
    print('Tenes un 25% de descuento')
else:
    print('No tenes ningun decuento')