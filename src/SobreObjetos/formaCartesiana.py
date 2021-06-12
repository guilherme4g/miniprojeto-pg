from src.Objetos.Plano import Plano

def formaCartesiana(plano):
    if type(plano) is not Plano: raise Exception("argumento reta não é uma reta valido")

    d = (plano.vetorNormal.x1 * (-plano.ponto.x1)) + (plano.vetorNormal.x2 * (-plano.ponto.x2))
    + (plano.vetorNormal.x3 * (-plano.ponto.x3))

    return [ plano.vetorNormal.x1, plano.vetorNormal.x2, plano.vetorNormal.x3, d]