from src.objetos.Vetor import Vetor
from src.objetos.Plano import Plano
from src.FerramentasBasicas.projecao import projecao

def componenteOrtogonal(vetor, plano):
    if type(vetor) is not Vetor: raise Exception("argumento vetor não é um vetor valido")
    if type(plano) is not Plano: raise Exception("argumento reta não é uma reta valido")

    #vetor resultante da projeção do vetor no vetor normal do plano
    componente = projecao(vetor, plano.vetorNormal)
    return componente