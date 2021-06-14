from src.Objetos.Reta import Reta

def normal(reta):
    if type(reta) is not Reta: raise Exception("argumento reta não é uma reta valido")
    return reta.vetorDiretor