from calculos import Calculo

def main():
    try:
        x = int(input("Digite o valor de X: "))
        y = int(input("Digite o valor de Y: "))
        
        calc1 = Calculo(x,y)
        
        soma = calc1.Somar()
        
        print(f"\nSOMA = {soma}")
    
    except ValueError:
        print("\nErro: Por favor, digite apenas números válidos!")

if __name__ == "__main__":
    main()