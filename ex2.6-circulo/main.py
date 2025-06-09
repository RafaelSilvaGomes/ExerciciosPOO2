from circulos import Circulo

def main():
    try:
        raio = float(input("Digite o valor do raio do círculo: "))
        
        circ1 = Circulo(raio)
        
        area = circ1.calcularArea()
        
        print(f"\nAREA = {area:.3f}")
    
    except ValueError:
        print("\nErro: Por favor, digite apenas números válidos!")

if __name__ == "__main__":
    main()