import json 
fichero1 = open("ejercicios6/productos.json")
fichero2 = open("ejercicios6/datos.json")
dicc1 = json.load(fichero1)
dicc2 = json.load(fichero2)
fichero1.close()
fichero2.close()
dicc1.update(dicc2)
fichero = open("ejercicios6/combinado.json", "w")
json.dump(dicc1, fichero)
fichero.close()
