class Salario:
    
    def __init__ (self, nome: str, valorH: float, horas: int):
        self.nome = nome
        self.valorH = valorH
        self.horas = horas

    def calcularPagamento(self) -> float:
        return self.valorH * self.horas
    
    