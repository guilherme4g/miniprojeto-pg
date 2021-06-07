from src import Vetor
import math

def norma(vetor):
    if type(vetor) is not Vetor: return "Vetor inserido não é um vetor valido"
    
    return abs(math.sqrt(vetor.x1*vetor.x1 + vetor.x2*vetor.x2 + vetor.x3*vetor.x3))
