import json;
rutaFichero = "ejRepaso2/horario.json"
'''
horario = {dia: clases}
clase = {"materia": , "hora"}
'''

def addHora():
    materia = input("Ingresa el nombre de la materia: ")
    dia = input("Ingresa el día de la semana: ")
    hora = 0
    while(hora < 1 or hora > 6):
        hora = int(input("Ingresa la hora (1-6): "))
    try:
        with open(rutaFichero) as fichero:
            info = json.load(fichero)
    except FileNotFoundError:
        with open(rutaFichero, "w") as fichero:
            json.dump({}, fichero)
            info = {}

    nuevaHora = {"materia": materia, "hora": hora}
    if dia in info:
        info[dia].append(nuevaHora)
    else:
        info.update({dia: [nuevaHora]})

    with open(rutaFichero, "w") as fichero:
        json.dump(info, fichero)
    
def mostrarHorarioDia():
    dia = input("Día a consultar: ")
    with open(rutaFichero) as fichero:
        info = json.load(fichero)
    if dia in info:
        print(info[dia])
    else:
        print("Día no encontrado")

def main():
    opcion = ""
    while (opcion != "3"):
        print("\n1. Añadir informacion al horario")
        print("\n2. Consultar horario")
        print("\n3. Salir\n")
        opcion = input("Opción: ")
        if (opcion == "1" ):
            addHora()
        elif (opcion == "2"):
            mostrarHorarioDia()
        elif (opcion == "3"):
            pass
        else:
            print("Selecciona una opción válida")
main()  

 