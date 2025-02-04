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

'''
devolucion = {"nombre": cantidadRestada}
'''
def actualizarInventario(devolucion):
    with open(rutaFichero) as fichero:
        inventario = json.load(fichero)
    for producto, cantidadDevuelta in devolucion.items():
        if producto in inventario:
            if cantidadDevuelta > inventario[producto]["cantidad"]:
                print("ERROR: Ventas insuficientes")
                return
            inventario[producto]["cantidad"] -= cantidadDevuelta
            print("Devolución realizada")
        else:
            print("ERROR: Producto no encontrado")
            
    with open(rutaFichero, "w") as fichero:
        json.dump(inventario, fichero)

guardarDatos()
entrada = ""
while(entrada != "3"):
    entrada = input("1. Total de ingresos\n2.Realizar devolución\n3.Salir")
    if (entrada == "1"):
        print(f"Total de ingresos: {totalIngresos()}")
    elif(entrada == "2"):
        nombreProducto = input("Nombre del producto: ")
        try:
            cantidadDevuelta = int(input("Cantidad devuelta: "))

        