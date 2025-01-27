archivo = open("ejercicios5/salida.txt", "w")
entrada = input('Introduce texto para salida.txt: ')
archivo.write(entrada)
archivo.close()