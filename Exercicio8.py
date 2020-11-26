# construa um analisador das 5 principais combinações de mãos do poker.
# Para isso utilize como base as classes descritas em:
# https://penseallen.github.io/PensePython2e/18-heranca.html
# considere como regra o poker fechado, em que a mão do jogador, já tem a combinação de 5 cartas :)

class Carta():
    nomes_naipe = ["Paus", "Ouros", "Copas", "Espadas"]
    numero_cartas = [None, "2", "3", "4", "5", "6", "7",
                     "8", "9", "10", "Valete", "Dama", "Rei", "Ás"]
    
    def __init__(self, naipe = 0, num = 2):
        self.naipe = naipe
        self.num = num
    
    
    def __str__(self):
        return (f"{Carta.numero_cartas[self.num]} "
                f"de {Carta.nomes_naipe[self.naipe]}")
    
    
    def __lt__(self, other):
        pass
    

class Baralho():
    def __init__(self):
        self.baralho = []
        for naipe in range(4):
            for numero in range(1,14):
                carta = Carta(naipe, numero)
                self.baralho.append(carta)
    
    def  __str__(self):
        baralho = []
        for carta in self.baralho:
            baralho.append(str(carta))
        return '\n'.join(baralho)



def limpar_tela():
    from os import name, system
    
    if name == 'nt': 
        system('cls') 
    else: 
        system('clear')


def verificar_mao(mao_jogador):
    cartas_na_mao = mao_jogador
    cartas_dict = []
    for carta in cartas_na_mao:
        cartas_dict.append(carta.__dict__)
    
    cartas_naipe = []
    cartas_numero = []
    for carta in cartas_dict:
        cartas_naipe.append(list(carta.values())[0])
        cartas_numero.append(list(carta.values())[1])
    
    paus = cartas_naipe.count(0)
    ouros = cartas_naipe.count(1)
    copas = cartas_naipe.count(2)
    espadas = cartas_naipe.count(3)
    
    dois = cartas_numero.count(1)
    tres = cartas_numero.count(2)
    quatro = cartas_numero.count(3)
    cinco = cartas_numero.count(4) 
    seis = cartas_numero.count(5) 
    sete = cartas_numero.count(6)
    oito = cartas_numero.count(7)
    nove = cartas_numero.count(8)
    dez = cartas_numero.count(9)
    onze = cartas_numero.count(10) 
    doze = cartas_numero.count(11)
    treze = cartas_numero.count(12)
    quatorze = cartas_numero.count(13)
    
    total_naipes = [paus, ouros, copas, espadas]
    total_numeros = [dois, tres, quatro, cinco, seis, sete, oito, nove,
                     dez, onze, doze, treze, quatorze]
    
    dupla = total_numeros.count(2)    
    # maior = max(cartas_numero)
    
    if quatorze == 1:
        sequencia = 1
    
    else:
        sequencia = 0
        
    for numero in total_numeros:
        if sequencia == 5:
            break
        
        if numero > 1:
            sequencia = 0
            break
        
        elif numero == 1:
            sequencia += 1
        
        else:
            sequencia = 0
            break
    
    if sequencia == 5 and 5 in total_naipes:
        resultado = "Você fez um Straigh Flush!"
        
    elif sequencia == 5:
        resultado = "Você fez um Straigh!"
        
    elif 4 in total_numeros:
        resultado = "Você fez uma Quadra!"
    
    elif 5 in total_naipes:
        resultado = "Você fez um Flush!"
    
    elif 3 in total_numeros and 2 in total_numeros:
        resultado = "Você fez um Full House!"
    
    elif 3 in total_numeros:
        resultado = "Você fez uma Trinca!"
    
    elif dupla == 2:
        resultado = "Você fez duas duplas!"
    
    elif 2 in total_numeros:
        resultado = "Você fez um par!"
    
    else:
        resultado = "Você não fez nada!"
    
    return resultado   


def main():
    from random import choices
    from time import sleep
    limpar_tela()
    msg = "Poker Python 2000"
    print("="*60)
    print(f"{msg:^60}")
    print("="*60)
    print()
    print("Dando as cartas...")
    sleep(1)
    limpar_tela()
    print("As cartas na sua mão são:\n")
    deck = Baralho()
    cartas_na_mao = choices(deck.baralho, k=5)
    
    for carta in cartas_na_mao:
        print(carta)
    
    print()
    print(verificar_mao(cartas_na_mao))

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
    