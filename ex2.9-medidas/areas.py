class Medidas:
    
    def __init__ (self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def areaQuadrado(self) -> float:
        return self.a**2
        
    def areaTriangulo(self) -> float:
        return (self.a*self.b)/2
    
    def areaTrapezio(self) -> float:
        return (self.a + self.b)*(self.c/2)
    
    
        