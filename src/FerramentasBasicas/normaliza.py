from src.Objetos.Vetor import Vetor
import math

def normaliza(vetor):
     if type(vetor) is not Vetor: raise Exception("Vetor inserido não é um vetor valido")
     return abs(math.sqrt(vetor.x1*vetor.x1+vetor.y1*vetor.x1+vetor.y1*vetor.y1))