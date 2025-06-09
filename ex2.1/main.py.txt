from terreno import Terreno

def main():
    try:
        largura = float(input("Digite a largura do terreno: "))
        comprimento = float(input("Digite o comprimento do terreno: "))
        valor = float(input("Digite o valor do m2: "))
        
        terreno1 = Terreno(largura, comprimento, valor)
        
        areaTerreno = terreno1.calcularArea()
        precoTerreno = terreno1.calcularPreco()
        
        print(f"\nÁrea do terreno = {areaTerreno:.2f}")
        print(f"Preço do terreno = {precoTerreno:.2f}")
    
    except ValueError:
        print("\nErro: Por favor, digite apenas números válidos!")

if __name__ == "__main__":
    main()