from duracao import Tempo

def main():
    try:
        segundos = int(input("Digite a duração em segundos: "))

        duracao1 = Tempo(segundos)
        
        h,m,s = duracao1.converterSegundos()
        
        print(f"{h}:{m}:{s}")
    
    except ValueError:
        print("\nErro: Por favor, digite apenas números válidos!")

if __name__ == "__main__":
    main()