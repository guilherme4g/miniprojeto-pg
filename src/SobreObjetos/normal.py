from src.Objetos.Plano import Plano

def normal(plano):
    if type(plano) is not Plano: raise Exception("argumento plano não é um plano valido")
    return plano.vetorNormal