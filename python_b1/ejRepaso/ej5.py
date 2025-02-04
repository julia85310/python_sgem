import json
def datosMayores():
    with open("ejRepaso/personas.json") as fichero:
        personas = json.load(fichero)
    personaAlta = None 
    personaMayor = None
    for persona, valor in personas.items():
        if personaMayor is None or (valor["edad"] > personas[personaMayor]["edad"]):
            personaMayor = persona
        if personaAlta is None or (valor["altura"] > personas[personaAlta]["altura"]):
            personaAlta = persona
    print("Persona mayor: " + str(personaMayor))
    print("Persona más alta: " + str(personaAlta))


        
personasLista = [
    ("Pepa", 30, 1.65),
    ("Juan", 66, 1.5),
    ("Sara", 14, 1.42),
    ("Mario", 18, 1.7),
    ("Pedro", 20, 1.77)       
    ]
personasDict = {}
for persona in personasLista:
    personasDict.update({persona[0]:{"edad": persona[1], "altura":persona[2]}})
with open("ejRepaso/personas.json", "w") as fichero:
    json.dump(personasDict, fichero)

datosMayores()