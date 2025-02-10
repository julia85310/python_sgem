class SerVivo:
    def __init__(self, nombre, energia):
        self.nombre = nombre
        self.energia = energia

    def mostrarEstado(self):
        print(f"{self.nombre} - Energía: {self.energia}")
class Animal(SerVivo):
    def __init__(self, nombre, energia):
        super().__init__(nombre, energia)
    
    def mover(self):
        if self.energia > 0:
            self.energia -= 5 
            print(f"{self.nombre} se ha movido y gastó 5 de energía.")
        else:
            print(f"{self.nombre} está demasiado cansado para moverse.")

    def comer(self, planta):
        if planta.energia > 0:
            self.energia += 10
            planta.energia -= 10
            print(f"{self.nombre} ha comido {planta.nombre} y ganó 10 de energía.")
        else:
            print(f"{planta.nombre} no tiene suficiente energía para ser comida.")
class Planta(SerVivo):  
    def __init__(self, nombre, energia):
        super().__init__(nombre, energia)
    
    def crecer(self):
        self.energia += 5 
        print(f"{self.nombre} ha crecido y ganó 5 de energía.")

def main():
    animal = Animal("Conejo", 30)
    planta = Planta("Hierba", 20)
    
    for dia in range(1, 7):
        print(f"Día {dia}")
        animal.mover()
        animal.comer(planta)
        planta.crecer()
        
        animal.mostrarEstado()
        planta.mostrarEstado()
        

main()