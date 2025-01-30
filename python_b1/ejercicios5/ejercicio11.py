def addNota():
    nota = input("Ingresa la nueva nota: ")
    with open("notas.txt", "a") as archivo:
        archivo.write(nota + "\n")
        print("Nota añadida")

def leerNotas():
    with open("notas.txt", "r") as archivo:
        notas = archivo.readlines()
        for nota in notas:
            print(nota.strip())

def buscarNota():
    palabra = input("Ingresa la palabra clave para buscar: ")
    with open("notas.txt", "r") as archivo:
        notas = archivo.readlines()
        encontrada = False
        for nota in notas:
            if palabra in nota:
                print(nota.strip())
                encontrada = True
    if (not encontrada):
        print("No se ha encontrado ninguna nota")

def borrarNota():
    notaAEliminar = input("Ingresa la nota que deseas borrar: ")
    encontrada = False
    with open("notas.txt", "r") as archivo:
        notas = archivo.readlines()
    with open("notas.txt", "w") as archivo:
        for nota in notas:
            if nota.strip() != notaAEliminar:
                archivo.write(nota)
            else:
                encontrada = True
    if (not encontrada):
        print("No se ha encontrado ninguna nota")

def main():
    while True:
        print("\n1. Añadir nueva nota")
        print("2. Leer todas las notas")
        print("3. Buscar nota")
        print("4. Borrar nota")
        print("5. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            addNota()
        elif opcion == "2":
            leerNotas()
        elif opcion == "3":
            buscarNota()
        elif opcion == "4":
            borrarNota()
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")

main()
