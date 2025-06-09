from pagamentos import Pagamento

def main():
    try:
        preco = float(input("Preço unitário do produto: "))
        qtde = int(input("Quantidade comprada: "))
        pago = float(input("Dinheiro recebido: "))
        
        pag1 = Pagamento(preco, qtde, pago)
        
        troco = pag1.Troco()
        
        print(f"\nTROCO = {troco:.2f}")
    
    except ValueError:
        print("\nErro: Por favor, digite apenas números válidos!")

if __name__ == "__main__":
    main()