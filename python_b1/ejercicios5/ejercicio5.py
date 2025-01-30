archivo = open("ejercicios5/datos.csv")
contenido = [linea.strip() for linea in archivo.readlines()]
archivo.close()

datos = []
claves = contenido[0].split(",")

for fila in range(1, len(contenido)):
    valores = contenido[fila].split(",")
    diccionario = dict(zip(claves, valores))
    datos.append(diccionario)

print(datos)
    