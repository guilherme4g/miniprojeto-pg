from src.FerramentasBasicas.eLI import eLI
class Base:
    def __init__(self,v1, v2, v3):
        assert eLI(v1, v2, v3)
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3