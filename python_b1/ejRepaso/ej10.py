from datetime import datetime
import json
rutaFichero = "ejRepaso/temperaturas.json"
# temperaturas = {ayer: temp, hoy: temp}
def getTemperaturas():
    with open(rutaFichero) as fichero:
        return json.load(fichero)

def addTemperatura(temperatura):
    temperaturas = getTemperaturas()
    hoy = datetime.today().strftime("%Y-%m-%d")
    if hoy in temperaturas:
        print("ERROR: Temperatura de hoy ya registrada")
    else:
        temperaturas.update({hoy:temperatura})
    with open(rutaFichero, "w") as fichero:
        json.dump(temperaturas, fichero)
    print("Temperatura de hoy registrada")
    
def mostrarPromedioUltimaSemana():
    temperaturas = getTemperaturas()
    claves = list(temperaturas.keys())
    sumaSemanal = 0
    for i in range(1, 8):
        sumaSemanal += temperaturas[claves[len(claves) - i]]
    print(f"Temperatura media de los últimos 7 días: {round(sumaSemanal/7, 2)}")


def main():
    entrada = ""
    while(entrada != "3"):
        entrada = input("1. Nuevo registro\n2. Promedio de temperaturas\n3. Salir\n")
        if (entrada == "1"):
            try:
                temperaturaHoy = float(input("Introduce la temperatura de hoy: ").strip())
                addTemperatura(temperaturaHoy)
            except:
                print("ERROR: Temperatura(numero) esperada")
        elif(entrada == "2"):
            mostrarPromedioUltimaSemana()
        else:
            if(entrada != "3"):
                print("Selecciona una opción válida")
main()
