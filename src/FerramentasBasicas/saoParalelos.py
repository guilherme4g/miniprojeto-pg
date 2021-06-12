from src.Objetos.Vetor import Vetor

def saoParalelos(vetor1, vetor2):
    if type(vetor1) is not Vetor: raise Exception("vetor1 não é um vetor valido")
    if type(vetor2) is not Vetor: raise Exception("vetor2 não é um vetor valido")

    #Para serem paralelos existe alfa cujo vetor1 = vetor2*alfa
    #Logo vetor1/vetor2 = alfa
    alfa1 = vetor1.x1/vetor2.x1
    alfa2 = vetor1.x2/vetor2.x2
    alfa3 = vetor1.x3/vetor2.x3

    return alfa1 == alfa2 and alfa3 == alfa2