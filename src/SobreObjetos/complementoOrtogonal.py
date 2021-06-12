from src.Objetos.Reta import Reta
from src.Objetos.Plano import Plano
from src.SobreObjetos.eParalelo import eParalelo

def complementoOrtogonal(argumento1, argumento2):  
    if type(argumento1) is Reta:
        reta = argumento1
    elif type(argumento1) is Plano:
        plano = argumento1
    else: raise Exception("argumento 1 está invalido")
    
    if type(argumento2) is Reta:
        reta = argumento2
    elif type(argumento2) is Plano:
        plano = argumento2
    else: raise Exception("argumento 2 está invalido")

    return eParalelo(plano.vetorNormal, reta)
