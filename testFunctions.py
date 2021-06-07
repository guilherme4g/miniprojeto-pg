from src.objetos.Ponto import Ponto
from src import Vetor, produtoEscalar, eLI, Base

# Tetando função produtoEscalar com vetor invalido
vetor1 = Vetor(4,2,3)
vetor2 = Vetor(4,2,-1)


# Tetando função produtoEscalar com vetor invalido
vetor1 = Vetor(2,2,0)
vetor2 = Vetor(0,5,-3)
vetor3 = Vetor(4,4,1)

eli = eLI(vetor1,vetor2,vetor3)

Base(vetor1, vetor2, vetor3)

ponto = Ponto(3,2, 2.3)

print(ponto)