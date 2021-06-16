import math
from src.Objetos.Vetor import Vetor
from src.Objetos.Plano import Plano
from src.Objetos.Reta import Reta
from src.FerramentasBasicas.produtoVetorial import  produtoVetorial
from src.Objetos.Ponto import Ponto
from src.Intersecoes.intersecaoRetaPlano import intersecaoRetaPlano
from src.FerramentasBasicas.projecao import projecao

#vertor = ponto1 - ponto2
def get_vetor_by_pontos(ponto1, ponto2):
    vetor = Vetor(ponto1.x1 - ponto2.x1, ponto1.x2 - ponto2.x2, ponto1.x3 - ponto2.x3)
    return vetor

def get_normal_by_vetores(v1, v2, v3):
    v = produtoVetorial(v1, v2)
    v = produtoVetorial(v, v3)
    return v

def intersecaoTriangulo(reta, triangulo):
    ab = get_vetor_by_pontos(triangulo.x1, triangulo.x2)
    bc = get_vetor_by_pontos(triangulo.x2, triangulo.x3)
    ca = get_vetor_by_pontos(triangulo.x3, triangulo.x1)

    plano = Plano(triangulo.x1, get_normal_by_vetores(ab, bc, ca))
    objeto = intersecaoRetaPlano(reta, plano)
    if objeto is Ponto:
        d = objeto
        return d

    