"""função que encontra o angulo entre dois vetores dados"""
import math

def projecao(v1, v2):
    quadrado1 = v1[0]**2
    quadrado2 = v1[1]**2
    quadrado3 = v1[2]**2
    norma1 = math.sqrt(quadrado1 + quadrado2+ quadrado3)

    quadrado21 = v2[0]**2
    quadrado22 = v2[1]**2
    quadrado23 = v2[2]**2
    norma2 = math.sqrt(quadrado21 + quadrado22+ quadrado23)

    produto = v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]

    print(round(math.degrees(math.acos(produto/(norma1*norma2))), 3))

projecao([2, 5, 7], [3, 8, 6])
