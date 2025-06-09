from math import sqrt

class Retangulo:
    
    def __init__ (self, base: float, altura: float):
        self.base = base;
        self.altura = altura;
        
    def calcularArea(self) -> float:
        return self.base * self.altura
    
    def calcularPerimetro(self) -> float:
        return (self.base*2) + (self.altura*2)
    
    def calcularDiagonal(self) -> float:
        return sqrt(self.base**2 + self.altura**2)
    
        