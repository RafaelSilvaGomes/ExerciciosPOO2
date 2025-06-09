from retangulo import Retangulo

def main():
    try:
        base = float(input("Digite a base do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
        
        retan1 = Retangulo(base, altura)
        
        areaRetangulo = retan1.calcularArea()
        periRetangulo = retan1.calcularPerimetro()
        diagRetangulo = retan1.calcularDiagonal()
        
        print(f"\nÁREA = {areaRetangulo:.4f}")
        print(f"PERÍMETRO = {periRetangulo:.4f}")
        print(f"DIAGONAL = {diagRetangulo:.4f}")
    
    except ValueError:
        print("\nErro: Por favor, digite apenas números válidos!")

if __name__ == "__main__":
    main()