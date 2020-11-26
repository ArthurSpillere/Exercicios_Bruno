# Faça um programa que simule um lançamento de dados. 
# Lance o dado 100 vezes e armazene os resultados em um vetor. 
# Depois, mostre quantas vezes cada valor foi conseguido.
# Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados. 
def limpar_tela():
    from os import name, system
    
    if name == 'nt': 
        system('cls') 
    else: 
        system('clear')


def main():
    from time import sleep
    from random import randint
    limpar_tela()
    msg = "Jogo dos dados!"
    print("="*60)
    print(f"{msg:^60}")
    print("="*60)
    print()
    sleep(1)
    print("Jogando os Dados!")
    sleep(2)
    limpar_tela()
    print("="*60)
    print()
    lista_jogadas = []
    
    for i in range(100):
        lista_jogadas.append(randint(1,6))
    
    print(f"Foram lançados {i+1} dados. Resultado:\n")
    
    for contador in range(1,7):
        
        print(f"Foram lançados {lista_jogadas.count(contador)}"
              f" dados com a face {contador}")           
    
    print()
    print("="*60)
    
    
if __name__ == "__main__":
    while True:
        main()
        
        resposta = input("\nDeseja jogar novamente? [S/N]\n"
                            "")[0].upper().strip()

        if resposta in "SN" and resposta != " " and resposta != "":
            if resposta == "S":
                continue
            else:
                break
        
        else:
            print("Você digitou uma entrada inválida! Tente novamente.")
            continue

    print("Obrigado por usar nossos serviços!")