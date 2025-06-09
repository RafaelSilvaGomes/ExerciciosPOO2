class Consumo:
    
    def __init__ (self, distancia: int, combustivel: float):
        self.distancia = distancia
        self.combustivel = combustivel

    def calcularConsumo(self) -> float:
        return self.distancia / self.combustivel
    
    
        
    