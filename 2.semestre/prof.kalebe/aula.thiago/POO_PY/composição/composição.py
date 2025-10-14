#basicamente uma classe não existe sem a outra, se eu excluir a classe carro o motor deixa de existir


import random

class Motor:
    def __init__(self, pot, comb):
        self.chassis = random.randrange(0,1000)
        self.potencia= pot
        self.combustivel= comb

    def get_combustivel(self):
        return self.combustivel
    
class Carro:
    def __init__ (self, modelo, potencia_motor, combustivel):
        self.modelo=modelo 
        self.motor= Motor(potencia_motor,combustivel)# composição