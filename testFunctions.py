from src.Objetos.Base import Base
from src.FerramentasBasicas.eLI import eLI
from src.Objetos.Triangulo import Triangulo
from src.Objetos.Reta import Reta
from src.Objetos.Ponto import Ponto
from src.Objetos.Esfera import Esfera
from src.Objetos.Plano import Plano
from src.SobreObjetos.projecao import projecao
from src import Vetor, produtoEscalar, norma, produtoVetorial, saoParalelos, componenteOrtogonal, complementoOrtogonal, intersecaoEsfera

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

#Teste de triangulo válido

ponto1 = Ponto(0,0,0)
ponto2 = Ponto(0,0,1)
ponto3 = Ponto(1,0,0)

triangulo = Triangulo(ponto1, ponto2, ponto3)

#teste projeçao sobre retaponto1 = Ponto(3, 2, 9)
ponto1 = Ponto(3, 2, 9)
reta = Reta(ponto1, vetor2)
v = projecao(vetor1, reta)
print(v.x1)

#teste componente ortogonal
plano = Plano(ponto1, vetor1)
componente = componenteOrtogonal(vetor2, plano)
print(f'{componente.x1}, {componente.x2}, {componente.x3}')

#teste de complementoOrtogonal
x = complementoOrtogonal(plano, reta)
y = complementoOrtogonal(reta, plano)
print(f'{x} : {y}')

#teste intersecaoEsfera
def print_ponto(ponto):
    print(f'x:{ponto.x1}, y:{ponto.x2}, z:{ponto.x3}')
centro = Ponto(0, 1, 3)
raio = 4
esfera = Esfera(centro, raio)
ponto = Ponto(0, 0, 0)
vetor = Vetor(0, 1, 0)
reta = Reta(ponto, vetor)
objeto = intersecaoEsfera(reta, esfera)
if type(objeto) is Ponto:
    print_ponto(objeto)
elif objeto != 0:
    print_ponto(objeto[0])
    print_ponto(objeto[1])