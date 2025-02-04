import json
def crearLibros():
    libros = {
    1: {"título": "1984", "autor": "George Orwell", "año": 1949, "precio": 12.99},
    2: {"título": "Cien años de soledad", "autor": "Gabriel García Márquez", "año": 1967, "precio": 15.50},
    3: {"título": "El señor de los anillos", "autor": "J.R.R. Tolkien", "año": 1954, "precio": 22.75},
    4: {"título": "Orgullo y prejuicio", "autor": "Jane Austen", "año": 1813, "precio": 10.99},
    5: {"título": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "año": 1605, "precio": 18.00}
    }

    with open("ejRepaso/libros.json", "w") as fichero:
        json.dump(libros, fichero)      

def leerLibros():
    with open("ejRepaso/libros.json") as fichero:
        libros = json.load(fichero)
    for clave in libros:
        libros[clave]["precio"] = libros[clave]["precio"] * 1.03
    with open("ejRepaso/libros.json", "w") as fichero:    
        json.dump(libros, fichero)

crearLibros()
leerLibros()
