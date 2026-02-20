lista_de_la_compra = ["Leche", "Arroz", "Jamon"]

for item in lista_de_la_compra:
    print(f'Hoy voy a comprar {item}')


frase = "Hola, hoy estoy aprendiendo Python"
vocales = ['a', 'e', 'i', 'o', 'u'] #tambien podria ser vocales = "aeiou"
vocales_encontradas = 0

for letra in frase:
    if letra in vocales:
        print(f"Encontre una '{letra}'")
        vocales_encontradas +=1
    
print(f'Vocales encontras: {vocales_encontradas}')