# Faça um programa que gera uma lista dos números primos existentes entre 1 e 
# um número inteiro informado pelo usuário. 

def limpar_tela():
    from os import name, system
    
    if name == 'nt': 
        system('cls') 
    else: 
        system('clear')


def main():
    from time import sleep
    limpar_tela()
    msg = "Gerador de primos! Os números mesmo...!"
    print("="*60)
    print(f"{msg:^60}")
    print("="*60)
    
    numero_final = int(input("Digite um número para ver os primos\n"
                             "entre 0 e este número:\n"))
    
    limpar_tela()
    print("Calculando...")
    sleep(2)
    limpar_tela()
    todos_numeros = [num for num in range(2, numero_final+1)]
    primos = todos_numeros[:]
        
    for divisor in todos_numeros:
        for numero in primos:
            if divisor > (numero/2):
                continue
            elif numero % divisor == 0:
                primos.remove(numero)
    
    print("="*60)
    print(f"\nOs números primos entre 1 e {numero_final} são:\n")
    if len(primos) == 0:
        print("Não há primos entre esses números!\n")
    else:
        for pos, resultado in enumerate(primos):
            if pos == len(primos)-1:
                print(f"{resultado} - FIM\n")
            else:
                print(f"{resultado} - ", end = "")
    print("="*60)
    
    
if __name__ == "__main__":
    while True:
        main()
        
        resposta = input("Deseja fazer nova operação? [S/N]\n"
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