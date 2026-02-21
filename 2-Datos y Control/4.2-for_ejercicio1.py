#Ejemplo
'''texto_usuario = 'Hola, me llamo Nacho. Tu como te llamas?'

#Output esperado luego de hacer el ejercicio:
espacios = 7
puntos = 1
comas = 1'''


texto_usuario = input('Introduce un texto: ')
espacios = 0
puntos = 0
comas = 0

for letra in texto_usuario:
    if letra == ' ':
        espacios +=1
    elif letra == '.':
        puntos += 1
    elif letra == ',':
        comas += 1

print(f'espacios: {espacios}')
print(f'Puntos: {puntos}')
print(f'Comas: {comas}')
    


