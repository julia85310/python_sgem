banco = {}

def updateSaldo(user, cantidad):
    if (user in banco):
        if (cantidad < 0 and cantidad > banco[user]):
            print("Fondos insuficientes")
        banco[user] = banco[user] + cantidad
    else:
        print("Usuario no encontrado")

def depositar():
    user = input("Introduce el usuario: ")
    try:
        cantidad = int(input("Introduce la cantidad a depositar: "))
        updateSaldo(user, cantidad)
        print("Operación realizada")
    except Exception:
        print("Cantidad inválida")

def retirar():
    user = input("Introduce el usuario: ")
    try:
        cantidad = int(input("Introduce la cantidad a retirar: "))
        updateSaldo(user, -cantidad)
        print("Operación realizada")
    except Exception:
        print("Cantidad inválida")
    
def consultarSaldo():
    user = input("Introduce el usuario: ")
    if (user in banco):
        print(f"Fondos: {banco[user]}")
    else:
        print("Usuario no encontrado")


def main():
    opcion = ""
    while (opcion != "4"):
        print("1. Consultar fondos")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Salir\n")
        opcion = input("Opción: ")
        if (opcion == "1" ):
            consultarSaldo()
        elif (opcion == "2"):
            depositar()
        elif (opcion == "3"):
            retirar()
        elif (opcion == "4"):
            pass
        else:
            print("Selecciona una opción válida")
main()