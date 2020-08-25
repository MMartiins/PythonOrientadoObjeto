class Cliente:
        def __init__(self, nome):
            self.__nome = nome


        #Aparentemente vc acha q ta chamando um get sem colocar o get na frente e achando que ta chamando um atributo, mas é um metodo. GET
        @property
        def nome(self):
            print("chamando @property nome()")
            return self.__nome.title()

        #Aparentemente vc acha q ta chamando um set sem colocar o set na frente e achando que ta chamando um atributo, mas é um metodo. SETTER
        @nome.setter
        def nome(self, nome):
            print("chamando setter nome()")
            self.__nome = nome