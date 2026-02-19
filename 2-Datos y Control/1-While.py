respuesta = None

while respuesta != "A" and respuesta != "B" and respuesta !="C":
    respuesta = input('Que opciones preferis? [A, B, C]: ')

if respuesta =="A":
    print('Elegiste bien')
elif respuesta == "B":
    print('podrias haber elegido mejor')
else:
    print('Elegiste la peor respuesta')