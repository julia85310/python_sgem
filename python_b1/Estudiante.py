class Estudiante:
    def __init__(self, nombre, calificaciones):
        self.nombre = nombre
        self.calificaciones = calificaciones

    def calcularPromedio(self):
        if len(self.calificaciones) == 0:
            print("No hay calificaciones registradas")
            return 0.0
        return sum(self.calificaciones) / len(self.calificaciones)


estudiante1 = Estudiante("Ana", [5, 10, 6, 9])
promedio = estudiante1.calcularPromedio()
print("El promedio de " + estudiante1.nombre + " es de " + str(promedio))