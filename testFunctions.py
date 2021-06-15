from src.FerramentasBasicas.saoOrtogonais import saoOrtogonais
from src.Objetos.Base import Base
from src.FerramentasBasicas.eLI import eLI
from src.Objetos.Triangulo import Triangulo
from src.Objetos.Reta import Reta
from src.Objetos.Ponto import Ponto
from src.Objetos.Esfera import Esfera
from src.Objetos.Plano import Plano
from src.SobreObjetos.projecao import projecao
from src import Vetor, produtoEscalar, norma, produtoVetorial, saoParalelos, componenteOrtogonal, complementoOrtogonal, intersecaoEsfera, formaCartesiana, cosseno, normalize   

# ** Ferramentas Basicas **
# Testando função produtoEscalar - valor esperado 32 - ok
vetor1 = Vetor(1, 2, 3)
vetor2 = Vetor(1, 5, 7)
print(f"Produto Escalar dos vetores ({vetor1.x1},{vetor1.x2},{vetor1.x3}) e ({vetor2.x1},{vetor2.x2},{vetor2.x3}): ",produtoEscalar(vetor1, vetor2))

#Testando função norma - valor esperado 5 - ok
vetor1 = Vetor(0,3,4)
print(f"Norma do vetor ({vetor1.x1},{vetor1.x2},{vetor1.x3}): ", norma(vetor1))

#Testando função cosseno - valor esperado é aproximadante 0.64 - ok
vetor1 = Vetor(1, 2, 3)
vetor2 = Vetor(4, 2, 1)
print(f"Cosseno entre os vetores ({vetor1.x1},{vetor1.x2},{vetor1.x3}) e ({vetor2.x1},{vetor2.x2},{vetor2.x3}): ",cosseno(vetor1, vetor2))

#Testando produto vetorial - vetor esperado (-8,4,0) - ok
vetor1 = Vetor(1, 2, 3) 
vetor2 = Vetor(1, 2, -1)
vetor3 = produtoVetorial(vetor1, vetor2)
print(f"Produto vetorial dos vetores ({vetor1.x1},{vetor1.x2},{vetor1.x3}) e ({vetor2.x1},{vetor2.x2},{vetor2.x3}): ({vetor3.x1},{vetor3.x2},{vetor3.x3})")

#Testando função normalize - valor esperado 1 - ok
vetor1 = Vetor(0,3,4)
print(f"Norma depois de Normalizar o vetor ({vetor1.x1},{vetor1.x2},{vetor1.x3}): ", norma(normalize(vetor1)))

#Testando funcao saoParalelos - true - ok
vetor1 = Vetor(2,   6, -4) 
vetor2 = Vetor(-3, -9,  6)
print(f"Oos vetores ({vetor1.x1},{vetor1.x2},{vetor1.x3}) e ({vetor2.x1},{vetor2.x2},{vetor2.x3}) sao paralelos? ", saoParalelos(vetor1, vetor2))

#Testando funcao saoParalelos - false - ok
vetor1 = Vetor(-5, 3, 7) 
vetor2 = Vetor(6, -8, 2)
print(f"Oos vetores ({vetor1.x1},{vetor1.x2},{vetor1.x3}) e ({vetor2.x1},{vetor2.x2},{vetor2.x3}) sao paralelos? ", saoParalelos(vetor1, vetor2))

#Testando funcao saoOrtogonais - true - ok
vetor1 = Vetor(-1,  2,  5) 
vetor2 = Vetor( 3,  4, -1)
print(f"Oos vetores ({vetor1.x1},{vetor1.x2},{vetor1.x3}) e ({vetor2.x1},{vetor2.x2},{vetor2.x3}) sao ortogonais? ", saoOrtogonais(vetor1, vetor2))

#Testando funcao saoOrtogonais - false - ok
vetor1 = Vetor(-5, 3, 7) 
vetor2 = Vetor(6, -8, 2)
print(f"Oos vetores ({vetor1.x1},{vetor1.x2},{vetor1.x3}) e ({vetor2.x1},{vetor2.x2},{vetor2.x3}) sao ortogonais? ", saoOrtogonais(vetor1, vetor2))

# falta testar ou reorganizar de ferramentas basicas eLI, projecao, reflexao, saoOrtogonais


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

#teste de foma cartesiana reta
print(formaCartesiana(reta))