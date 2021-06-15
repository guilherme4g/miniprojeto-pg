from src.Objetos.Vetor import Vetor
from src.FerramentasBasicas.norma import norma

def normalize(vetor):
     if type(vetor) is not Vetor: raise Exception("Vetor inserido não é um vetor valido")
     
     mag = norma(vetor)
     if mag == 0: raise Exception("magnitude é zero")

     vetor.multEscalar((1/mag))
     return vetor

     