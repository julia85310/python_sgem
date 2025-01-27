class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def mostrarInfo(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")
class Coche(Vehiculo):
    def __init__(self, marca, modelo, numPuertas):
        super().__init__(marca, modelo)
        self.numPuertas = numPuertas

    def mostrarNumPuertas(self):
        print(f"El coche tiene {self.numPuertas} puertas.")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def mostrarTipo(self):
        print(f"La moto es de tipo: {self.tipo}.")

coche = Coche("Toyota", "Corolla", 4)
moto = Moto("Yamaha", "MT-07", "Deportiva")

coche.mostrarInfo()
coche.mostrarNumPuertas()

moto.mostrarInfo()
moto.mostrarTipo()