import json
try:
    fichero = open("ejercicios5/archivo1.txt")
    contenido = json.load(fichero)
    fichero.close()
    print("Archivo válido")
except json.JSONDecodeError as e:
    print("Archivo no válido")
