class Pagamento:
    
    def __init__ (self, preco: float, qtde: int, pago: float):
        self.preco = preco;
        self.qtde = qtde;
        self.pago = pago;
        
    def Troco(self) -> float:
        total = self.preco * self.qtde
        return self.pago - total
    
    
        
    
        