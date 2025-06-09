from math import pi

class Circulo:
    
    def __init__ (self, raio: float):
        self.raio = raio;

    def calcularArea(self) -> float:
        return pi * (self.raio**2)