from src import Vetor
from src import Ponto


class Plano:
    def __init__(self, ponto, vetorNormal):
        assert type(ponto) is Ponto
        assert type(vetorNormal) is Vetor
        self.ponto = ponto
        self.vetorNormal = vetorNormal