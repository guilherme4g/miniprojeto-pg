from src.Objetos.Vetor import Vetor

def produtoVetorial(vetor1, vetor2):
    if type(vetor1) is not Vetor: raise Exception("vetor1 não é um vetor valido")
    if type(vetor2) is not Vetor: raise Exception("vetor2 não é um vetor valido")

    x1 = (vetor1.x2* vetor2.x3) - (vetor1.x3*vetor2.x2)
    x2 = (vetor1.x3* vetor2.x1) - (vetor1.x1*vetor2.x3)
    x3 = (vetor1.x1* vetor2.x2) - (vetor1.x2*vetor2.x1)
    
    vetor = Vetor(x1, x2, x3)
    return vetor