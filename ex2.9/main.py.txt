from areas import Medidas

def main():
    try:
        A = float(input("Digite a medida A: "))
        B = float(input("Digite a medida B: "))
        C = float(input("Digite a medida C: "))

        medidas1 = Medidas(A, B, C)
        
        areaQ = medidas1.areaQuadrado()
        areaTri = medidas1.areaTriangulo()
        areaTra = medidas1.areaTrapezio()
        
        print(f"\nÁREA DO QUADRADO = {areaQ:.4f}")
        print(f"ÁREA DO TRIÂNGULO = {areaTri:.4f}")
        print(f"ÁREA DO TRAPÉZIO = {areaTra:.4f}")
    
    except ValueError:
        print("\nErro: Por favor, digite apenas números válidos!")

if __name__ == "__main__":
    main()