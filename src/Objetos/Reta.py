from src.Objetos.Vetor import Vetor
from src.Objetos.Ponto import Ponto
class Reta:
    def __init__(self, ponto, vetorDiretor):
        assert type(ponto) is Ponto
        assert type(vetorDiretor) is Vetor
        self.ponto = ponto
        self.vetorDiretor = vetorDiretor
