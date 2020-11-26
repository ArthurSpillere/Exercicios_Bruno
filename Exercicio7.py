# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

#     quantos espaços em branco existem na frase.
#     quantas vezes aparecem as vogais a, e, i, o, u.

def limpar_tela():
    from os import name, system
    
    if name == 'nt': 
        system('cls') 
    else: 
        system('clear')


def main():
    from time import sleep
    limpar_tela()
    msg = "Analisador de Frases!"
    print("="*60)
    print(f"{msg:^60}")
    print("="*60)
    print()
    
    frase = input("Entre com a frase aqui:\n").strip().lower()
    contadores = ("a", "e", "i", "o","u"," ",)
    limpar_tela()
    print("Analisando a frase...")
    sleep(2)
    limpar_tela()
    print("="*60)
    print()
    
    for verificador in contadores:
        if verificador != " ":
            print(f"Foram encontrados {frase.count(verificador)} "
                  f"letras {verificador}")
        
        else:
            print(f"Foram encontrados {frase.count(verificador)} "
                  "espaços em branco")
    
    print()
    print("="*60)
    
    
if __name__ == "__main__":
    while True:
        main()
        
        resposta = input("\nDeseja verificar outra frase? [S/N]\n"
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