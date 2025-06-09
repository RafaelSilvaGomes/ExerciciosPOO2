class Tempo:
    
    def __init__ (self, segundos: int):
        self.segundos = segundos

    def converterSegundos(self) -> tuple[int, int, int]:
        
        horas = self.segundos // 3600
        
        segundosRestantes = self.segundos % 3600
        
        minutos = segundosRestantes // 60
        
        segundos = segundosRestantes % 60
   
        return horas, minutos, segundos
        