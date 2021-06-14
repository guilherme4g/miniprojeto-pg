from src.Objetos.Base import Base
from src.FerramentasBasicas.eLI import eLI
from src.Objetos.Triangulo import Triangulo
from src.Objetos.Reta import Reta
from src.Objetos.Ponto import Ponto
from src.Objetos.Esfera import Esfera
from src.Objetos.Plano import Plano
from src.SobreObjetos.projecao import projecao
from src import Vetor, produtoEscalar, norma, produtoVetorial, saoParalelos, componenteOrtogonal, complementoOrtogonal, intersecaoEsfera, formaCartesiana, cosseno

# ** Ferramentas Basicas **
# Testando função produtoEscalar - valor esperado 32
vetor1 = Vetor(1, 2, 3)
vetor2 = Vetor(1, 5, 7)
print(f"Produto Escalar dos vetores ({vetor1.x1},{vetor1.x2},{vetor1.x3}) e ({vetor2.x1},{vetor2.x2},{vetor2.x3}): ",produtoEscalar(vetor1, vetor2))

#Testando função norma - valor esperado 5
vetor1 = Vetor(0,3,4)
print(f"Norma do vetor ({vetor1.x1},{vetor1.x2},{vetor1.x3}): ", norma(vetor1))

#Testando função cosseno - valor esperado é aproximadante 0.64
vetor1 = Vetor(1, 2, 3)
vetor2 = Vetor(4, 2, 1)
print(f"Cosseno entre os vetores ({vetor1.x1},{vetor1.x2},{vetor1.x3}) e ({vetor2.x1},{vetor2.x2},{vetor2.x3}): ",cosseno(vetor1, vetor2))

#Testando produto vetorial - vetor esperado (-8,4,0)
vetor1 = Vetor(1, 2, 3) 
vetor2 = Vetor(1, 2, -1)
vetor3 = produtoVetorial(vetor1, vetor2)
print(f"Produto vetorial dos vetores ({vetor1.x1},{vetor1.x2},{vetor1.x3}) e ({vetor2.x1},{vetor2.x2},{vetor2.x3}): ({vetor3.x1},{vetor3.x2},{vetor3.x3})")

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
vetor = Vetor(1, 1, 1)
reta = Reta(ponto, vetor)
objeto = intersecaoEsfera(reta, esfera)
if type(objeto) is Ponto:
    print_ponto(objeto)
elif objeto != 0:
    print_ponto(objeto[0])
    print_ponto(objeto[1])

forma = formaCartesiana(reta)
print(forma)