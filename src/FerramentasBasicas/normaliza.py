from src import Vetor
import math

def normaliza(vetor):
     if type(vetor) is not Vetor: return "Vetor inserido não é um vetor valido"
     
     "normaliza"
     return abs(math.sqrt(vetor.x1*vetor.x1+vetor.y1*vetor.x1+vetor.y1*vetor.y1))