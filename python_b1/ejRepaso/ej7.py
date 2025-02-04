import json
listaPeliculas = [
    ("Interstellar", 2014, "Ciencia ficción"),
    ("Blade Runner 2049", 2017, "Ciencia ficción"),
    ("El Padrino", 1972, "Crimen"),
    ("El Padrino II", 1974, "Crimen"),
    ("Toy Story", 1995, "Animación"),
    ("Shrek", 2001, "Animación"),
    ("El Caballero de la Noche", 2008, "Acción")
]

dictPeliculas = {}
for pelicula in listaPeliculas:
    genero = pelicula[2]
    if genero not in dictPeliculas:
        dictPeliculas[genero] = []
    dictPeliculas[genero].append({
        "titulo": pelicula[0],
        "año": pelicula[1]
    })
    
with open("ejRepaso/peliculas.json", "w") as fichero:
    json.dump(dictPeliculas, fichero)

def buscarPorGenero(genero):
    with open("ejRepaso/peliculas.json") as fichero:
        dictPeliculas = json.load(fichero)
        return dictPeliculas.get(genero, -1)

entrada = ""   
while(entrada != "salir"):
    entrada = input("Busca peliculas por genero(salir para finalizar): ")
    if entrada != "salir":
        peliculas = buscarPorGenero(entrada)
        if peliculas == -1:
            print("Género no encontrado")
        else:
            print(peliculas)



