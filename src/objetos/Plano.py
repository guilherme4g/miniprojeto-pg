from src.objetos.Vetor import Vetor
from src.objetos.Ponto import Ponto


class Plano:
    def __init__(self, ponto, vetorNormal):
        assert type(ponto) is Ponto
        assert type(vetorNormal) is Vetor
        self.ponto = ponto
        self.vetorNormal = vetorNormal