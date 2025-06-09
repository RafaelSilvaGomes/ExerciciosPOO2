from salarios import Salario

def main():
    try:
        nome = str(input("Nome: "))
        valorH = float(input("Valor por hora: "))
        horas = float(input("Horas trabalhadas: "))
        
        func1 = Salario(nome, valorH, horas)
        
        salario = func1.calcularPagamento()
        
        print(f"\nO pagamento para {func1.nome} deve ser {salario:.2f}")
    
    except ValueError:
        print("\nErro: Por favor, digite apenas números válidos!")

if __name__ == "__main__":
    main()