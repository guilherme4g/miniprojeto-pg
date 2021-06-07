from src import Vetor,produtoEscalar

def saoOrtogonais (vetor1, vetor2):
    if type(vetor1) is not Vetor: raise Exception("vetor1 não é um vetor valido") 
    if type(vetor2) is not Vetor: raise Exception("vetor2 não é um vetor valido") 

    return produtoEscalar(vetor1, vetor2) == 0
