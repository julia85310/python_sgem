import json
fichero = open("ejercicios6/estudiantes.json")
estudiantes = json.load(fichero)
fichero.close()
estudianteBrillante = estudiantes[0]
suma = 0
for estudiante in estudiantes:
    suma += estudiante["calificacion"]
    if(estudianteBrillante["calificacion"] < estudiante["calificacion"]):
        estudianteBrillante = estudiante
media = suma / len(estudiantes)
print("Mejor estudiante: " + str(estudianteBrillante))
print("Media: " + str(media))