#Crear un programa que pase de grados Fahrenheit a Celsius (Formula = (X-32)*5/9 = Y)
grados_f = 45

grados_c = (grados_f - 32) * 5/9

print(grados_c)

#Crear un programa que cambie de libras a euros, preguntar cuantas libras se quieren cambiar y despues mostrar el valor en euros
#1 libra = 1.15 euros
libras = float(input('Cuantas libras queres cambiar: '))
tasa_de_cambio = 1.15
euros = libras * tasa_de_cambio

print(f'Serian {euros} Euros')
