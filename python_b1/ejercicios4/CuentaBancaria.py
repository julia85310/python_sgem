class CuentaBancaria :
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, dinero):
        self.saldo += dinero
        print("Cantidad ingresada: " + str(dinero))
        print("Saldo actual: " + str(self.saldo))

    def retirar(self, dinero):
        if (self.saldo < dinero):
            print("Saldo insuficiente")
        else:
            self.saldo -= dinero
            print("Cantidad retirada: " + str(dinero))
            print("Saldo actual: " + str(self.saldo))
        

    def consultar(self):
        print("Saldo actual: " + str(self.saldo))

cuenta = CuentaBancaria ("Pepa", 25)
cuenta.consultar()
cuenta.retirar(26)
cuenta.depositar(1)
cuenta.retirar(26)
