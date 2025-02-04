import json
def datosMayores():
    with open("ejRepaso/personas.json") as fichero:
        personas = json.load(fichero)
        
        for persona, valor in personas.items():


        
personasLista = [
    ("Pepa", 30, 1.65),
    ("Juan", 66, 1.8),
    ("Sara", 14, 1.42),
    ("Mario", 18, 1.7),
    ("Pedro", 20, 1.77)       
    ]
personasDict = {}
for persona in personasLista:
    personasDict.update({persona[0]:{"edad": persona[1], "altura":persona[2]}})
with open("ejRepaso/personas.json", "w") as fichero:
    json.dump(personasDict, fichero)