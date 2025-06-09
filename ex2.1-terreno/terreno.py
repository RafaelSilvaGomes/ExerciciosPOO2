class Terreno:
    
    def __init__ (self, largura: float, comprimento: float, valor: float):
        self.largura = largura;
        self.comprimento = comprimento;
        self.valor = valor;
        
    def calcularArea(self) -> float:
        return self.largura * self.comprimento
    
    def calcularPreco(self) -> float:
        area = self.largura * self.comprimento
        return area * self.valor
    

        
        