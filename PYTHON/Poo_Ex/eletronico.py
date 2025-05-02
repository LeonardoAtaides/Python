class Eletronico:
    def __init__(self, nome ):
        self._nome = nome
        self._ligado = False
    
    def ligar (self, nome):
        if not self._ligado:
            self._ligado = True
            print(f'{nome} Ligado')
    
    def desligar (self, nome):
        if self._ligado:
            self._ligado = False
            print(f'{nome} Desligado')

class SmartPhone(Eletronico):
    ...