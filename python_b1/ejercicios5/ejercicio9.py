archivo = open("ejercicios5/log.txt")
contenido = archivo.readlines()
archivo.close()

contenidoLimpio = []
for lineaAComprobar in contenido:
    repetida = False
    for lineaNueva in contenidoLimpio:
        if(lineaAComprobar == lineaNueva):
            repetida = True
            break
    if (not repetida):
        contenidoLimpio.append(lineaAComprobar)

archivo = open("ejercicios5/limpio.txt", "w")
archivo.writelines(contenidoLimpio)
archivo.close()
