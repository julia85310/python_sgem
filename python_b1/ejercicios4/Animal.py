class Animal:
    def hacer_sonido(cls, sonido):
        print(sonido)

class Perro(Animal):
    def hacer_sonido(cls):
        print("Guau")
    
class Gato(Animal):
    def hacer_sonido(cls):
        print("Miau")

firulais = Perro()
firulais.hacer_sonido()

medianoche = Gato()
medianoche.hacer_sonido()