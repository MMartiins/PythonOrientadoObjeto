class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def tranfere(self, valor, destino):
        self.sacar(valor)
        destino.deposita(valor)
    @property
    def saldo(self):
        return self.__saldo
    @property
    def titular(self):
        return self.__titular
    @property
    def limite(self):
        return self.__limite
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    # Quando todos os objetos usa a mesma coisa e essa coisa não faz parte fortemente dentro do objeto, então é aceitavel deixar essa coisa estatica
    @staticmethod
    def condigo_banco():
        return "001"

    @staticmethod
    def condigos_bancos():
        return {"BB":"001", "Caixa":"104", "Bradesco":"237"}