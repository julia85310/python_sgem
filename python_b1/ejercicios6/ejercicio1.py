import json 
fichero = open("ejercicios6/datos.json")
dict = json.load(fichero)
fichero.close()
print(dict["nombre"])