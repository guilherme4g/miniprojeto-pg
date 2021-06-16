import copy
from src.Objetos.Reta import Reta
from src.Objetos.Plano import Plano
from src.FerramentasBasicas.produtoEscalar import  produtoEscalar
from src.SobreObjetos.formaCartesiana import formaCartesianaPlano

def intersecaoRetaPlano(reta, plano):
    if type(reta) is not Reta: raise Exception("reta não é um reta valido")
    if type(plano) is not Reta: raise Exception("plano não é um plano valido")

    denominador = produtoEscalar(reta.vetorDiretor , plano.vetorNormal)
    if (denominador == 0): raise Exception("sao paralelos")

    formaCartesiana = formaCartesianaPlano(plano)

    numerador = produtoEscalar(reta.ponto , plano.vetorNormal) + formaCartesiana[3]

    t = numerador / denominador

    vetorDiretorMult = copy.copy(reta.vetorDiretor)
    vetorDiretorMult.escalar(t)

    pontoIntersecao = copy.copy(reta.ponto)
    pontoIntersecao.x1 = pontoIntersecao.x1 + vetorDiretorMult.x1
    pontoIntersecao.x2 = pontoIntersecao.x2 + vetorDiretorMult.x2
    pontoIntersecao.x3 = pontoIntersecao.x3 + vetorDiretorMult.x3


