import math
from src.Objetos.Vetor import Vetor

def projecao(v1, v2):

    produto = v1.x1 * v2.x2 + v1.x2 * v2.x2 + v1.x3 * v2.x3

    quadrado21 = v2.x1**2
    quadrado22 = v2.x2**2
    quadrado23 = v2.x3**2
    norma2 = math.sqrt(quadrado21 + quadrado22 + quadrado23)

    const = produto/norma2
    vetor2 = [v2.x1, v2.x2, v2.x3]
    
    # v é o vetor projetado em forma de array
    v = list(map(lambda x: round(x * const, 3), vetor2))
    vetor = Vetor(v[0], v[1], v[2])
    return vetor