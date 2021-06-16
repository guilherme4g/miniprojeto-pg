import copy
from src.Objetos.Vetor import Vetor
from src.Objetos.Plano import Plano
from src.FerramentasBasicas.projecao import projecao as projecaoOrtogonal

def projecaoVetorPlano(vetor, plano):
    if type(vetor) is not Vetor: raise Exception("argumento vetor não é um vetor valido")
    if type(plano) is not Plano: raise Exception("argumento plano não é uma plano valido")

    vetorProj = projecaoOrtogonal(plano.vetorNormal, vetor)
    projPlane = copy.copy(vetor)

    projPlane.x1 = projPlane.x1 - vetorProj.x1
    projPlane.x2 = projPlane.x2 - vetorProj.x2
    projPlane.x3 = projPlane.x3 - vetorProj.x3

    return projPlane