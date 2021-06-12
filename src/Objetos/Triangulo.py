import math
from src.Objetos.Ponto import Ponto

class Triangulo:
    def __init__(self, ponto1, ponto2, ponto3):
        assert type(ponto1) is Ponto
        assert type(ponto2) is Ponto
        assert type(ponto3) is Ponto
        validaPontosDoTriangulo(ponto1, ponto2, ponto3)
        self.ponto1 = ponto1
        self.ponto2 = ponto2
        self.ponto3 = ponto3

def validaPontosDoTriangulo(ponto1, ponto2, ponto3):
    verticeA = math.pow((math.pow((ponto1.x1 - ponto2.x1), 2) + math.pow((ponto1.x2 - ponto2.x2), 2) + math.pow((ponto1.x3 - ponto2.x3), 2)), 0.5)
    verticeB = math.pow((math.pow((ponto1.x1 - ponto3.x1), 2) + math.pow((ponto1.x2 - ponto3.x2), 2) + math.pow((ponto1.x3 - ponto3.x3), 2)), 0.5)
    verticeC = math.pow((math.pow((ponto2.x1 - ponto3.x1), 2) + math.pow((ponto2.x2 - ponto3.x2), 2) + math.pow((ponto2.x3 - ponto3.x3), 2)), 0.5)

    print(verticeA)
    print(verticeB)
    print(verticeC)
    print(math.fabs(verticeB - verticeC) < verticeA)

    if (math.fabs(verticeB - verticeC) < verticeA and verticeA < verticeB + verticeC) is False: raise Exception("Pontos informados não formam um triangulo válido")
    if (math.fabs(verticeA - verticeC) < verticeB and verticeB < verticeA + verticeC) is False: raise Exception("Pontos informados não formam um triangulo válido")
    if (math.fabs(verticeA - verticeB) < verticeC and verticeC < verticeA + verticeB) is False: raise Exception("Pontos informados não formam um triangulo válido")
