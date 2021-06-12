from src.Objetos.Vetor import Vetor
from src.Objetos.Ponto import Ponto


class Plano:
    def __init__(self, ponto, vetorNormal):
        assert type(ponto) is Ponto
        assert type(vetorNormal) is Vetor
        self.ponto = ponto
        self.vetorNormal = vetorNormal