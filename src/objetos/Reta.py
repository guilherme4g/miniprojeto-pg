from src import Vetor
from src import Ponto


class Reta:
    def __init__(self, ponto, vetorDiretor):
        assert type(ponto) is Ponto
        assert type(vetorDiretor) is Vetor
        self.ponto = ponto
        self.vetorDiretor = vetorDiretor
