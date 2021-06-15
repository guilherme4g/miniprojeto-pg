from src.Objetos.Vetor import Vetor
from src.FerramentasBasicas.projecao import projecao

def reflexao(vetor1, vetor2):
    if type(vetor1) is not Vetor: raise Exception("argumento vetor1 não é um vetor valido")
    if type(vetor2) is not Vetor: raise Exception("argumento vetor2 não é um vetor valido")

    vetorProj = projecao(vetor1, vetor2)
    vetorProj.multEscalar(2)

    vetorReflexao = vetor1

    vetorReflexao.x1 = vetorReflexao.x1 - vetorProj.x1
    vetorReflexao.x2 = vetorReflexao.x2 - vetorProj.x2
    vetorReflexao.x3 = vetorReflexao.x3 - vetorProj.x3

    return vetorReflexao