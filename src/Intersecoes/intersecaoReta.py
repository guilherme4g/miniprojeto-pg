from src.Objetos.Vetor import Vetor
from src.Objetos.Reta import Reta
from src.Objetos.Ponto import Ponto
from src.FerramentasBasicas.produtoEscalar import  produtoEscalar
from src.SobreObjetos.eParalelo import  eParalelo
from src.SobreObjetos.formaCartesiana import  formaCartesiana
 

def get_parametro(c, ponto, vetor):
    v1 = Vetor(ponto.x1, ponto.x2, ponto.x2)
    v2 = Vetor(c[0], c[1], c[2])
    d = produtoEscalar(vetor, v2)
    if d != 0:
        return (produtoEscalar(v1, v2) + c[3])/d
    else:
        return 0


def intersecaoReta(reta1, reta2):
    if type(reta1) is not Reta: return "reta1 não é um reta valido"
    if type(reta2) is not Reta: return "reta2 não é um reta valido"

   
    vetor = reta1.vetorDiretor
    c = formaCartesiana(reta2)

    if(eParalelo(reta1.vetorDiretor, reta2)):
        
        equacao = c[0][0]*vetor.x1 + c[0][1]*vetor.x2 + c[0][2]*vetor.x3 + c[0][3]
        equacao2 = c[1][0]*vetor.x1 + c[1][1]*vetor.x2 + c[1][2]*vetor.x3 + c[1][3]
        if(equacao2 == 0 and equacao ==0):
            return reta2
        else: 
            return 0
    else:
        ponto = reta1.ponto
        t1 = get_parametro(c[0], ponto, vetor)
        t2 = get_parametro(c[1], ponto, vetor)
        if t1 == t2:
            return Ponto(ponto.x1 + vetor.x1*t1, ponto.x2 + vetor.x2*t1, ponto.x3 + vetor.x3*t1)
        else:
            return 0