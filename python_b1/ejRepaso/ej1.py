def function(texto):
    try:
        int(texto)
        return "Error: String esperado. Numero recibido"
    except:
        mayorContador = 1

    recuentoPalabras = {}
    recuentoPalabrasOrdenado = {}
    palabras = texto.split()
    for palabra in palabras:
        if palabra not in recuentoPalabras:
            apariciones = palabras.count(palabra)
            if apariciones > mayorContador:
                mayorContador = apariciones
            recuentoPalabras.update({palabra: apariciones})
    for i in range(mayorContador, 0, -1):
        for palabra, apariciones in recuentoPalabras.items():
            if (apariciones == i):
                recuentoPalabrasOrdenado.update({palabra: apariciones})
    return recuentoPalabrasOrdenado

texto = input("Introduce un texto: ")
print(function(texto))




    