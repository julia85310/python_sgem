claveAdmin = 123
products = []
carrito = []

def addProduct(nombre, stock, precio):
    global claveAdmin, products
    clave = int(input('Introduce la clave de administrador: '))
    if (clave == claveAdmin):
        product = {'nombre': nombre, 'stock': stock, 'precio': precio}
        if (not any(productExistente['nombre'] == product['nombre'] for productExistente in products)):
            products.append(product)
        else:
            print('Producto ya existente')
    else:
        print('Clave incorrecta')

def updateProductStock(nombre, stockNuevo):
    global claveAdmin, products
    clave = int(input('Introduce la clave de administrador: '))
    if (clave == claveAdmin):
        existe = False
        for product in products:
            if(product['nombre'] == nombre):
                product['stock'] = stockNuevo
                existe = True
                break
        if (not existe):
            print('No existe el producto ' + nombre)
    else:
        print('Clave incorrecta')


def updateProductPrecio(nombre, precioNuevo):
    global claveAdmin, products
    clave = int(input('Introduce la clave de administrador: '))
    if (clave == claveAdmin):
        existe = False
        for product in products:
            if(product['nombre'] == nombre):
                product['precio'] = precioNuevo
                existe = True
                break
        if (not existe):
            print('No existe el producto ' + nombre)
    else:
        print('Clave incorrecta')

def mostrarInventario():
    global products
    print(products)

def addToCart(nombre, cantidad):
    global carrito, products
    existe = False
    for product in products:
        if(product['nombre'] == nombre):
            existe = True
            precio = product['precio']
            if(product['stock'] < cantidad):
                print('No hay stock suficiente')
            else:
                carrito.append({'nombre': nombre, 'precio': precio, 'cantidad': cantidad})
            break
    if(not existe):
        print('No existe el producto ' + nombre)

def deleteFromCart(nombre, cantidad):
    global carrito
    if(len(carrito) == 0):
        print('Carrito vacio')
    existe = False
    for product in carrito:
        if(product['nombre'] == nombre):
            existe = True
            if(product['cantidad'] < cantidad):
                print('Solo tienes ' + str(product['cantidad']))
            elif(product['cantidad'] == cantidad):
                carrito.remove(product)
            else:
                product['cantidad'] = product['cantidad'] - cantidad
            break
    if(not existe):
        print('No existe el producto ' + nombre + ' en el carrito')

def costeTotalCarrito():
    global carrito
    if(len(carrito) == 0):
        print('Carrito vacio')
        return 0
    suma = 0
    for product in carrito:
        suma = suma + (product['cantidad'] * product['precio'])
    return suma

def comprar():
    global carrito, products
    if(len(carrito) == 0):
        print('Carrito vacio')
    for productCart in carrito:
        for productTienda in products:
            if(productCart['nombre'] == productTienda['nombre']):
                productTienda['stock'] = productTienda['stock'] - productCart['cantidad']
                break
    carrito = []
    print('Compra realizada')
            


def mostrarMenu():
    print('1. Agregar producto')
    print('2. Actualizar precio de un producto')
    print('3. Actualizar stock de un producto')
    print('4. Mostrar Inventario')
    print('5. Añadir producto al carrito')
    print('6. Retirar producto del carrito')
    print('7. Mostrar el contenido del carrito')
    print('8. Coste total del carrito')
    print('9. Comprar')
    print('10. Salir')
    option = int(input(''))
    return option


def main():
    option = -1
    while(option != 10):
        option = mostrarMenu()
        if(option == 1):
            nombre = input('Introduce el nombre del nuevo producto: ')
            stock = int(input('Introduce su stock: '))
            precio = int(input('Introduce su precio: '))
            addProduct(nombre, stock, precio)
        elif(option == 2):
            nombre = input('Introduce el nombre del producto: ')
            precio = int(input('Introduce su nuevo precio: '))
            updateProductPrecio(nombre, precio)
        elif(option == 3):
            nombre = input('Introduce el nombre del producto: ')
            stock = int(input('Introduce su nuevo stock: '))
            updateProductStock(nombre, stock)
        elif(option == 4):
            mostrarInventario()
        elif(option == 5):
            nombre = input('Introduce el nombre del producto: ')
            cantidad = int(input('Introduce la cantidad a añadir: '))
            addToCart(nombre, cantidad)
        elif(option == 6):
            nombre = input('Introduce el nombre del producto: ')
            cantidad = int(input('Introduce la cantidad a retirar: '))
            deleteFromCart(nombre, cantidad)
        elif(option == 7):
            print(carrito)
        elif(option == 8):
            costeTotal = costeTotalCarrito()
            print('Coste total del carrito: ' + str(costeTotal))
        elif(option == 9):
            comprar()
        elif(option == 10):
            print('Saliendo...')
        else:
            print('Opción inválida')
main()       