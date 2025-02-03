import json
dicc = {"id": 1, 
        "nombre": "esponja",
        "precio": 1.2}
fichero = open("ejercicios6/productos.json", "w")
json.dump(dicc, fichero)
fichero.close()