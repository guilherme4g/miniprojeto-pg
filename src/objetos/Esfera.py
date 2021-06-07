from src import Ponto

class Esfera:
    def __init__(self, ponto, raio):
        assert type(ponto) is Ponto
        assert raio > 0
        self.ponto = ponto
        self.raio = raio