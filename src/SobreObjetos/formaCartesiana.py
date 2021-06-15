from src.Objetos.Plano import Plano
from src.Objetos.Reta import Reta

def formaCartesiana(objeto):
    if type(objeto) is Plano:
        return formaCartesianaPlano(objeto)
    elif type(objeto) is Reta:
        return formaCartesianaReta(objeto)
    else: raise Exception("argumento inválido")


def formaCartesianaPlano(plano):

    d = (plano.vetorNormal.x1 * (-plano.ponto.x1)) + (plano.vetorNormal.x2 * (-plano.ponto.x2))
    + (plano.vetorNormal.x3 * (-plano.ponto.x3))

    return [ plano.vetorNormal.x1, plano.vetorNormal.x2, plano.vetorNormal.x3, d]

def x0(v, p):
    a = v.x2/v.x1
    b = -1
    c = 0
    d = p.x2 - ((v.x2/v.x1)*p.x1)
    e = v.x3/v.x1
    f = 0
    g = -1
    h = p.x3 - ((v.x3/v.x1)*p.x1)
    return ([a, b, c, d], [e, f, g, h])

def y0(v, p):
    a = -1
    b = v.x1/v.x2
    c = 0
    d = p.x1 - ((v.x1/v.x2)*p.x2)
    e = 0
    f = v.x3/v.x2
    g = -1
    h = p.x3 - ((v.x3/v.x2)*p.x2)
    return ([a, b, c, d], [e, f, g, h])

def formaCartesianaReta(reta):
    v = reta.vetorDiretor
    p = reta.ponto

    if v.x1 != 0:
        return x0(v, p)
    elif v.x2 != 0:
        return y0(v, p)
    else:
        return ([1, 0, 0, p.x1], [0, 1, 0, p.x2])

