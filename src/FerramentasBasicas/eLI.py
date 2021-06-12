from src.Objetos.Vetor import Vetor

def eLI (vetor1, vetor2, vetor3):
    if type(vetor1) is not Vetor: raise Exception("vetor1 não é um vetor valido") 
    if type(vetor2) is not Vetor: raise Exception("vetor2 não é um vetor valido")
    if type(vetor3) is not Vetor: raise Exception("vetor3 não é um vetor valido")

    det = vetor1.x1*(vetor2.x2*vetor3.x3 - vetor3.x2*vetor2.x3) - vetor1.x2*(vetor2.x1*vetor3.x3 - vetor3.x1*vetor2.x3) + vetor1.x3*(vetor2.x1*vetor3.x2 - vetor3.x1*vetor2.x2)
    return det != 0