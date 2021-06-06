from src import Vetor,produtoEscalar

def produtoEscalar (vetor1, vetor2):
    if type(vetor1) is not Vetor: return "vetor1 não é um vetor valido"
    if type(vetor2) is not Vetor: return "vetor2 não é um vetor valido"

    return True if produtoEscalar(vetor1, vetor2) == 0 else False
