banco = {"Juan": 300, "Lola": 10, "José": 50}
userNow = ""
def updateSaldo(cantidad):
    global banco
    if (userNow in banco):
        if (cantidad < 0 and cantidad > banco[userNow]):
            print("Fondos insuficientes")
        banco[userNow] = banco[userNow] + cantidad
    else:
        print("Usuario no encontrado")

def depositar():
    try:
        cantidad = int(input("Introduce la cantidad a depositar: "))
        updateSaldo(cantidad)
        print("Operación realizada")
    except Exception:
        print("Cantidad inválida")

def retirar():
    try:
        cantidad = int(input("Introduce la cantidad a retirar: "))
        updateSaldo(-cantidad)
        print("Operación realizada")
    except Exception:
        print("Cantidad inválida")
    
def consultarSaldo():
    if (userNow in banco):
        print(f"Fondos: {banco[userNow]}")
    else:
        print("Usuario no encontrado")

def login():
    global userNow
    user = input("Introduce el usuario: ")
    if (user not in banco):
        print("Usuario no encontrado")
    else:
        userNow = user
        
def main():
    global userNow
    salir = ""
    while(salir != "y"):
        login()
        if (userNow != ""):
            opcion = ""
            while (opcion != "4"):
                print("1. Consultar fondos")
                print("2. Depositar")
                print("3. Retirar")
                print("4. Cerrar Sesión\n")
                opcion = input("Opción: ")
                if (opcion == "1" ):
                    consultarSaldo()
                elif (opcion == "2"):
                    depositar()
                elif (opcion == "3"):
                    retirar()
                elif (opcion == "4"):
                    userNow = ""
                else:
                    print("Selecciona una opción válida")
        userNow = ""
        salir = input("¿Deseas salir?y/n: ")
                
    
main()