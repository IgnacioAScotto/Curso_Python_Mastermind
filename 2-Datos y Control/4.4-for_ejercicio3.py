'''
#Numero elegido por el usuario: 2, output esperado:
2x1 = 2
2x2 = 4
2x3 = 6
2x4 = 8
2x5 = 10
2x6 = 12
2x7 = 14
2x8 = 16
2x9 = 18
2x10 = 20
'''

numero_multiplicador = int(input('Introduce un numero: '))

for numero in range(1, 11):
    multiplicacion = numero * numero_multiplicador
    print(f'{numero_multiplicador} x {numero} = {multiplicacion}')