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

def ej5():
    cadena = 'Julia Rueda Romero'
    print(cadena.count('a'))

def ej6():
    cadena = 'Julia Rueda Romero'
    print(cadena.index('a'))

def ej7():
    cadena = 'Julia Rueda Romero'
    posPrimerEspacio = cadena.index(' ');
    cadenaSinNombre = cadena[posPrimerEspacio + 1:]
    print(cadenaSinNombre.index('a'))

def ej8():
    nums = [1, 2, 3, 4, 5]
    nums.append(6)
    nums.pop(nums.index(3))
    print(nums)

def ej9():
    nums = [1, 2, 3, 4, 5]
    nums.pop(3)
    print(nums)

def ej10():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    nums.pop()
    nums.pop()
    nums.pop()
    nums.pop(0)
    nums.pop(0)
    nums.pop(0)
    print(nums)

def ej11():
    nums = [23, 43, 1, 90, 242, 1, 34, 5.43, 5, 90]
    nums.sort(reverse=True)
    print(nums)

def ej12():
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [6, 7, 8, 9, 10]
    nums = nums1 + nums2
    print(nums)

def ej13():
    nums = [1, 2, 3, 4, 5]
    nums.append(3.1416)
    nums.sort()
    print(nums)

def ej14():
    names = ["Juan", "Maria", "Carlos"]
    cadena = names[0] + ',' + names[1] + ',' + names[2]
    print(cadena)

def ej15():
    nums = (1, 2, 3)
    print(nums * 2)

def ej16():
    yo = {'nombre': 'Julia', 
          'edad': 19, 
          'ciudad': 'Lebrija'}
    print(yo)

def ej17():
    yo = {'nombre': 'Julia',
           'edad': 19, 
           'ciudad': 'Lebrija',
           'nickname': 'julia85310'}
    yo.pop('ciudad')
    print(yo)

def ej18():
    dic = {'numeros': [1, 2, 3, 4, 5]}
    dic['numeros'].append(7)
    dic['numeros'][0] = 0
    print(dic)

def ej19():
    tupla = (':)', 4, 0)
    dic = {tupla[0]: tupla[1], tupla[2]: 'sol'}
    print(dic)

def ej20():
    dic = {'Julia': (9, 9, 8)}
    print(dic)

ej20()