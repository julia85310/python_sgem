def ej1():
    numero1 = 2.1
    print(numero1, type(numero1))
    numero2 = int(numero1)
    print(numero2, type(numero2))
    numero3 = float(numero2)
    print(numero3, type(numero3))

def ej2():
    cadena = "Pedro"
    print(cadena * 3)


def ej3():
    cadena = 'Sistemas de Gestión Empresarial'
    indicePrimerEspacio = cadena.index(" ")
    a = cadena[:indicePrimerEspacio]
    print(a, len(a))
    indiceSegundoEspacio = cadena.index(" ", indicePrimerEspacio + 1)
    b = cadena[indicePrimerEspacio + 1 : indiceSegundoEspacio]
    print(b, len(b))
    c = cadena.upper()
    print(c, len(c))
    d = cadena.replace(" ", "")
    print(d, len(d))

def ej4():
    cadena = 'S,G,E'
    lista = cadena.split(',')
    print(lista)
    
ej4()