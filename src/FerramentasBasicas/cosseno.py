"""função que encontra o angulo entre dois vetores dados"""
import math
from src.Objetos.Vetor import Vetor

def projecao(v1, v2):
    quadrado1 = v1.x1**2
    quadrado2 = v1.x2**2
    quadrado3 = v1.x3**2
    norma1 = math.sqrt(quadrado1 + quadrado2+ quadrado3)

    quadrado21 = v2.x1**2
    quadrado22 = v2.x2**2
    quadrado23 = v2.x3**2
    norma2 = math.sqrt(quadrado21 + quadrado22+ quadrado23)

    produto = v1.x1 * v2.x1 + v1.x2 * v2.x2 + v1.x3 * v2.x3

    print(round(math.degrees(math.acos(produto/(norma1*norma2))), 3))

projecao([2, 5, 7], [3, 8, 6])
