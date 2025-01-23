class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def agregarExistencias(self, cantidadAgregar):
        self.cantidad += cantidadAgregar
        print(f"Cantidad agregada: {cantidadAgregar}")
        print(f"Stock inicial: {self.cantidad - cantidadAgregar}, Stock final: {self.cantidad}")
        
    def quitarExistencias(self, cantidadQuitar):
        if (self.cantidad < cantidadQuitar):
            print(f"Stock insuficiente: {self.cantidad}")
        else:
            self.cantidad -= cantidadQuitar
            print(f"Cantidad quitada: {cantidadQuitar}")
            print(f"Stock inicial: {self.cantidad + cantidadQuitar}, Stock final: {self.cantidad}")

    def mostrarInfo(self):
        print(f"Nombre: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}")

producto1 = Producto("Papas", 2, 10)
producto1.agregarExistencias(11)
producto1.quitarExistencias(30)
producto1.quitarExistencias(10)
producto1.mostrarInfo()

