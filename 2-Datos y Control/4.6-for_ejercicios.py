'''numero de usuario: 
numeros = [1, 2, 3, 4, 5, 6]

Outuput
numero_mas_chico = 1
numero_mas+grande = 6 '''

numeros_de_usuario = []

numero_introducido = int(input('Introduce un numero a la lista: '))
numeros_de_usuario.append(numero_introducido)

while input("Desea introducir otro numero? [S/N]: ") == "S":
    numero_introducido = int(input('Introduce un numero a la lista: '))
    numeros_de_usuario.append(numero_introducido)

print(numeros_de_usuario)

print(f'El numero mas grande es: {max(numeros_de_usuario)}')
print(f'El numero mas chico es: {min(numeros_de_usuario)}')

