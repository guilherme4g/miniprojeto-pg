from src.objetos.Vetor import Vetor
from src.objetos.Reta import Reta

def eParalelo(vetor, reta):
    if type(vetor) is not Vetor: raise Exception("argumento vetor não é um vetor valido")
    if type(reta) is not Reta: raise Exception("argumento reta não é uma reta valido")

    t1 = (vetor.x1 - reta.vetorDiretor.x1) / reta.ponto.x1
    t2 = (vetor.x2 - reta.vetorDiretor.x2) / reta.ponto.x2
    t3 = (vetor.x3 - reta.vetorDiretor.x3) / reta.ponto.x3

    return t1 == t2 and t2 == t3