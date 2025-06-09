from consumos import Consumo

def main():
    try:
        distancia = int(input("Distancia percorrida (KM): "))
        combustivel = float(input("Combustível gasto: "))

        viagem1 = Consumo(distancia, combustivel)
        
        consumo = viagem1.calcularConsumo()
        
        print(f"\nConsumo médio = {consumo:.3f}")
    
    except ValueError:
        print("\nErro: Por favor, digite apenas números válidos!")

if __name__ == "__main__":
    main()