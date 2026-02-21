'''
Ejercicio 2:
texto_usuario: 'Hola, me llamo Nacho. Vos como te llamas?

Output esperado:
mayusculas = 3
'''

texto_usuario = input('Introduci un texto: ')
mayusculas = 0

for letra in texto_usuario:
    if letra.lower() != letra:
        mayusculas += 1
print(f'Mayusculas: {mayusculas}')