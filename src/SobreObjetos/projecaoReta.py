from src.objetos.Vetor import Vetor
from src.objetos.Reta import Reta
from src.FerramentasBasicas.projecao import projecao

def projecaoReta(vetor, reta):
    if type(vetor) is not Vetor: raise Exception("argumento vetor não é um vetor valido")
    if type(reta) is not Reta: raise Exception("argumento reta não é uma reta valido")

    v = projecao(vetor,reta.vetorDiretor)
    return v