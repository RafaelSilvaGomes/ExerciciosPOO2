from pessoas import Pessoa

def main():
    try:
        print("Dados da primera pessoa: ")
        nome = str(input("Digite o Nome: "))
        idade = int(input("Digite a Idade: "))
        
        pessoa1 = Pessoa(nome, idade)
        
        print("Dados da segunda pessoa: ")
        nome = str(input("Digite o Nome: "))
        idade = int(input("Digite a Idade: "))
        
        pessoa2 = Pessoa(nome, idade)
        
        media = Pessoa.calcularMedia(pessoa1, pessoa2)
        
        print(f"\nA idade média de {pessoa1.nome} e {pessoa2.nome} é de {media:.1f}")
    
    except ValueError:
        print("\nErro: Por favor, digite apenas números válidos!")

if __name__ == "__main__":
    main()