import math
from src.Objetos.Vetor import Vetor
from src.Objetos.Ponto import Ponto
from src.FerramentasBasicas.norma import norma
from src.FerramentasBasicas.projecao import projecao

def mult_escalar_vetor(escalar, vetor):
    return Vetor(escalar*vetor.x1, escalar*vetor.x2, escalar*vetor.x3)

#ponto = vetor + ponto inicial
def get_ponto_by_vetor(projecao, ponto):
    ponto = Ponto(projecao.x1 + ponto.x1, projecao.x2 + ponto.x2, projecao.x3 + ponto.x3)
    return ponto

#vertor = ponto1 - ponto2
def get_vetor_by_pontos(ponto1, ponto2):
    vetor = Vetor(ponto1.x1 - ponto2.x1, ponto1.x2 - ponto2.x2, ponto1.x3 - ponto2.x3)
    return vetor

def intersecaoEsfera(reta, esfera):
    ac = get_vetor_by_pontos(esfera.ponto, reta.ponto)

    proj = projecao(ac, reta.vetorDiretor)
    x =math.pow(norma(ac),2)- math.pow(norma(proj), 2)

    if x > 0:
        distancia = math.sqrt(x)
    else: raise Exception("argumento")

    distancia = round(distancia)
    if distancia == esfera.raio:
        return get_ponto_by_vetor(proj, reta.ponto)
    elif distancia < esfera.raio:
        ponto = get_ponto_by_vetor(proj, reta.ponto)
    
        vetorCentroReta = get_vetor_by_pontos(ponto, esfera.ponto)
        
        escalar = math.sqrt(math.pow(esfera.raio,2) - math.pow(norma(vetorCentroReta), 2))/norma(reta.vetorDiretor)

        ponto1 = get_ponto_by_vetor(mult_escalar_vetor(escalar, reta.vetorDiretor), ponto)
        ponto2 = get_ponto_by_vetor(mult_escalar_vetor(-1*escalar, reta.vetorDiretor), ponto)
        return (ponto1, ponto2)
    else:
        return 0
