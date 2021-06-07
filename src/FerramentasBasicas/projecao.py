import math

def projecao(v1, v2):

    produto = v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]

    quadrado21 = v2[0]**2
    quadrado22 = v2[1]**2
    quadrado23 = v2[2]**2
    norma2 = math.sqrt(quadrado21 + quadrado22 + quadrado23)

    const = produto/norma2

    print(list(map(lambda x: round(x * const, 3), v2)))