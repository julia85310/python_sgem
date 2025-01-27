archivo = open("ejercicios5/datos.csv")
contenido = archivo.readlines()
archivo.close()
datos = []
claves = contenido[0].split(",")

for fila in contenido[1::]:
    diccionario = dict(zip(claves, fila))
    datos.append(diccionario)

print(datos)
    