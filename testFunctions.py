from src import Vetor, produtoEscalar, norma, produtoVetorial, saoParalelos

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

print(produtoEscalar(vetor1, vetor2))

#Testando função norma
vetor1 = Vetor(0,3,4)
print(norma(vetor1))

#Testando produto vetorial
vetor1 = Vetor(1, 2, 3)
vetor2 = Vetor(1, 2, -1)

vetor3 = produtoVetorial(vetor1, vetor2)

print(f'vetor3 => {vetor3.x1}, {vetor3.x2}, {vetor3.x3}')

#Testando se vetores são paralelos
vetor1 = Vetor(-3, 2, 1)
vetor2 = Vetor(-9, 7, 3)

print(saoParalelos(vetor1, vetor2))
