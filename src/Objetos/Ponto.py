class Ponto:
  def __init__(self, x1, x2, x3):
    assert isinstance(x1, (int, float))
    assert isinstance(x2, (int, float))
    assert isinstance(x3, (int, float))
    self.x1 = x1
    self.x2 = x2
    self.x3 = x3