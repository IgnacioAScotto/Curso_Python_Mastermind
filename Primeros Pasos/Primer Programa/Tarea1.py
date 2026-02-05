#Crear un programa que con 3 numeros dados por el usuario devuelva el mas grande y el mas chico

a = int(input('Decime un numero: '))
b = int(input('Decime un numero: '))
c = int(input('Decime un numero: '))

print(f'El numero mas grande ingresado es: {max(a,b,c)}')
print(f'El numero mas chico ingresado es: {min(a,b,c)}')