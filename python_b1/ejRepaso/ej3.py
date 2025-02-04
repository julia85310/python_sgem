def inputALista():
    esTexto = False
    while(not esTexto):
        texto = input("Dame texto: ")
        try:
            int(texto)
        except:
            esTexto = True
    palabras = texto.replace(",", "").replace(".", "").split()
    for palabra in palabras:
        palabra.lower()
    return palabras

print(inputALista())
    

