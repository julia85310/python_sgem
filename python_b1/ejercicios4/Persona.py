class Persona:
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    def saludar(self):
        print("Saludos, soy " + self.nombre + " y tengo " + str(self.edad) + " años")

    def informacion(self):
        print("Mido " + str(self.altura) + " m")


persona1 = Persona("Juan", 25, 1.75)
persona1.saludar()
persona1.informacion()
