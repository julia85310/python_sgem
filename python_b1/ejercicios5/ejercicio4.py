palabraBuscar = input('Palabra a buscar: ')
palabraSustituir = input('Palabra con la que sustituir: ')
archivo = open('ejercicios5/texto.txt', 'r+')
contenido = archivo.read()
contenido = contenido.replace(palabraBuscar, palabraSustituir)
archivo.seek(0)
archivo.write(contenido)
archivo.truncate()
archivo.close()
