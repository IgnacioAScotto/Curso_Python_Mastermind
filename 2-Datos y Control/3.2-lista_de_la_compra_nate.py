#Este es el ejericio que hizo Nate Gentile
lista_de_la_compra = []
input_de_usuario = None

print('Bienvenido a la lista de la compra')

while input_de_usuario != True:
    input_de_usuario = input('Que desea comprar? ([Q] para salir): ')
    if input_de_usuario == "Q":
        break
    elif input_de_usuario in lista_de_la_compra:
        print(f'{input_de_usuario} ya esta en la lista!')
    else:
        if input_de_usuario(f'Seguro que quiere agregar {input_de_usuario} a la lista de la compra? [S/N]') == "S":
            lista_de_la_compra.append(input_de_usuario)

print('La lista de la compra es:')
print(lista_de_la_compra)