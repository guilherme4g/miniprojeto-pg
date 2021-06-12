from src.Objetos.Ponto import Ponto


class Segmento:
    def __init__(self, ponto1, ponto2):
        assert type(ponto1) is Ponto
        assert type(ponto2) is Ponto
        self.ponto1 = ponto1
        self.ponto2 = ponto2