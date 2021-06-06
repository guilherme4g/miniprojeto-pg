from src import Vetor, produtoEscalar

# Tetando função produtoEscalar com vetor invalido
vetor1 = Vetor(4,2,3)
vetor2 = Vetor(4,2,-1)

print(produtoEscalar(vetor1, vetor2))

# Tetando função produtoEscalar com vetor invalido
vetor1 = Vetor(4,2,3)
vetor2 = "guilherme"

print(produtoEscalar(vetor1, vetor2))