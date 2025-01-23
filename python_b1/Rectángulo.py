class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    @property
    def area(self):
        return self.ancho * self.alto


rectangulo = Rectangulo(5, 10)
print("El área del rectángulo es " + str(rectangulo.area))
