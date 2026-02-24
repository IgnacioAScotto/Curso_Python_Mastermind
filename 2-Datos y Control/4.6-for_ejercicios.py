'''numero de usuario: 
numeros = [1, 2, 3, 4, 5, 6]

Outuput
numero_mas_chico = 1
numero_mas+grande = 6 '''

lista_numeros_usuario = []
agregar_numero = None

while agregar_numero != "Q":
    input_de_usuario = (input("Agrega un numero a la lista: ['Q' para salir]: "))
    if input_de_usuario == "Q":
        break
    elif input_de_usuario in lista_numeros_usuario:
        print(f"El nro {input_de_usuario} ya se encuentra en la lista")
    else:
        lista_numeros_usuario.append(input_de_usuario)
        print(f'Se agrego el numero {input_de_usuario} a la lista de numeros')

print(f'La lista de numeros es: {lista_numeros_usuario}')



