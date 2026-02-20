lista_compra = []

agregar_cosas = None

while agregar_cosas != "Q":

    agregar_cosas = input('Que desea comprar? ([Q] para salir): ')
    if agregar_cosas == "Q":
        print('\nLa lista de la compra es:\n'
            f'{lista_compra}')
    else:
        confirmacion = input(f'Seguro que desea agregar {agregar_cosas} a la lista?: [S/N]: ')
        if confirmacion == "S":
            if agregar_cosas in lista_compra:
                print(f'{agregar_cosas} ya esta en la lista!')
            else:
                lista_compra.append(agregar_cosas)
                print(f'{agregar_cosas} se agrego a la lista\n')

