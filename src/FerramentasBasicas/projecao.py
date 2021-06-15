from src.Objetos.Vetor import Vetor
from src.FerramentasBasicas.produtoEscalar import produtoEscalar

def projecao(vetor1, vetor2):
    if type(vetor1) is not Vetor: raise Exception("argumento vetor1 não é um vetor valido")
    if type(vetor2) is not Vetor: raise Exception("argumento vetor2 não é um vetor valido")
    
    escalar = produtoEscalar(vetor1, vetor2) / produtoEscalar(vetor2, vetor2)
    vetorProj = vetor2

    vetorProj.x1 = escalar * vetorProj.x1
    vetorProj.x2 = escalar * vetorProj.x2
    vetorProj.x3 = escalar * vetorProj.x3

    return vetorProj