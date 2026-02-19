respuesta = None

while respuesta != "A" and respuesta != "B" and respuesta !="C":
    respuesta = input('Que opciones preferis? [A, B, C]: ')
    print('Probando')


    print('Probando 2.0') #Esto sigue perteneciendo al while por la tabulacion
    print("Esto sigue siendo parte del bucle while.")


if respuesta =="A":
    print('Elegiste bien')
elif respuesta == "B":
    print('podrias haber elegido mejor')
elif respuesta =="B":
    print('Elegiste la peor respuesta')
else:
    print('No me diste una respuesta con sentido') #Esto no hace falta con el while, por lo que el else podria estar en el respuesta == "C"