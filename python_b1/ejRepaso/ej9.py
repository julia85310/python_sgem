import json
clientes = {
    "Juan": {
        "correo": "juan.perez@email.com",
        "compras": ["Olla a presión", "Batidora"]
    },
    "María": {
        "correo": "maria.lopez@email.com",
        "compras": ["Freidora", "Cafetera", "Licuadora"]
    },
    "Carlos": {
        "correo": "carlos.sanchez@email.com",
        "compras": ["Tetera"]
    }
}

with open("ejRepaso/clientes.json", "w") as fichero:
    json.dump(clientes, fichero)

def mayorComprador():
    with open("ejRepaso/clientes.json") as fichero:
        clientes = json.load(fichero)   
    nombreMayorComprador = None 
    for nombre, datos in clientes.items():
        if nombreMayorComprador is None or len(datos["compras"]) > len(clientes[nombreMayorComprador]["compras"]):
            nombreMayorComprador = nombre
    # si queremos la info: return clientes[nombreMayorComprador].items()
    return nombreMayorComprador

print(f"Mayor comprador: {mayorComprador()}")