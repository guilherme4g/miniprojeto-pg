from src.Objetos.Vetor import Vetor
from src.Objetos.Plano import Plano
from src.FerramentasBasicas.saoParalelos import saoParalelos

def eOrtogonal(vetor, plano):
    if type(vetor) is not Vetor: raise Exception("argumento vetor não é um vetor valido")
    if type(plano) is not Plano: raise Exception("argumento reta não é uma reta valido")

    return saoParalelos(vetor, plano.vetorNormal)