from src import Plano
import math

def intersecao(plano1,plano2):
    if type(plano1) is not Plano: return "plano1 não é um vetor valido"
    if type(plano2) is not Plano: return "plano2 não é um vetor valido"
    
    return abs(math.sqrt(plano1.x-plano2.y)*(plano1.z-plano2.w)-(plano2.w-plano1.x)*(plano2.y-plano1.x))