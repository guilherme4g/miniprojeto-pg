from src import Vetor

def produtoEscalar (vetor1, vetor2):
    if type(vetor1) is not Vetor: return "vetor1 não é um vetor valido"
    if type(vetor2) is not Vetor: return "vetor2 não é um vetor valido"

    return ((vetor1.x1 * vetor2.x1) + (vetor1.x2 * vetor2.x2) + (vetor1.x3 * vetor2.x3))

