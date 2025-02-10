class SerVivo:
    def __init__(self, nombre, energia):
        self.nombre = nombre
        self.energia = energia

class Animal(SerVivo):
    def __init__(self, nombre, energia):
        super().__init__(nombre, energia)

class Planta(SerVivo):  
    def __init__(self, nombre, energia):
        super().__init__(nombre, energia)

