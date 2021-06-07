from src.objetos.Vetor import Vetor
from src.objetos.Ponto import Ponto


class Reta:
    def __init__(self, ponto, vetorDiretor):
        assert type(ponto) is Ponto
        assert type(vetorDiretor) is Vetor
        self.ponto = ponto
        self.vetorDiretor = vetorDiretor
