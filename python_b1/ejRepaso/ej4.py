import json
rutaFichero = "ejRepaso/ventas.json"
def guardarDatos():
    ventas = {
        "tornillos": {"precio": 0.06, "cantidad":40},
        "clavos": {"precio": 0.02, "cantidad":30},
        "martillo": {"precio": 4, "cantidad":6},
        "llave": {"precio": 2.3, "cantidad":12},
        "cinta": {"precio": 1.2, "cantidad":24},
    }
    with open(rutaFichero, "w") as fichero:
        json.dump(ventas, fichero)

def totalIngresos():
    ingresos = 0
    with open(rutaFichero) as fichero:
        ventas = json.load(fichero)
    for producto, venta in ventas.items():
        ingresos += venta["precio"] * venta["cantidad"]
    return ingresos
