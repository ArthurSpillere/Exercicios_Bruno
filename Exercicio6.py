#######################################################################################################
# Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas,
# com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma.
# Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

#     8  3  4 
#     1  5  9
#     6  7  2

# Elabore uma função que identifica e mostra na tela todos os quadrados mágicos
# com as características acima. 
# Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado.
# Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3. 


def limpar_tela():
    from os import name, system
    
    if name == 'nt': 
        system('cls') 
    else: 
        system('clear')


def main():
    from time import sleep
    from itertools import permutations
    
    limpar_tela()
    msg = "Quadrado Mágico!"
    print("="*60)
    print(f"{msg:^60}")
    print("="*60)
    print("\nCalculando todas as possbilidades de Quadrados Mágicos 3x3")
    sleep(2)
    limpar_tela()
    
    num_quadrados_magicos = 0
    qm_lista = list(permutations([1,2,3,4,5,6,7,8,9]))
    
    print(len(qm_lista))
    for qm in qm_lista:
        soma = qm[0] + qm[1] + qm[2]
        contador = 0
        
        for i in range(0,7,3):
            if (qm[i] + qm[i+1] + qm[i+2]) == soma:
                contador += 1
            else:
                break
        
        if contador < 3:
            continue
        
        for i in range(3):
            if (qm[i] + qm[i+3] + qm[i+6]) == soma:
                contador += 1
            else:
                break 
                
        if contador < 6:
            continue
        
        for i in range(0,3,2):
            if (qm[0+i] + qm[4] + qm[8-i]) == soma:
                contador += 1

        if contador < 8:
            continue
        
        else:
            num_quadrados_magicos +=1
            print(f"\nQuadrador Mágico nº{num_quadrados_magicos}\n")
            print(f"{qm[0]} {qm[1]} {qm[2]}\n"
                    f"{qm[3]} {qm[4]} {qm[5]}\n"
                    f"{qm[6]} {qm[7]} {qm[8]}")

if __name__ == "__main__":
    while True:
        main()
        
        # não entendi muito bem a funcionalidade de usar novamente considerado que os números são os mesmos
        resposta = input("\nDeseja usar novamente? [S/N]\n"
                            "")[0].upper().strip()

        # Joguei novamente e o código "trava" no quadrado nº 6 e inicia novamente do 1

        if resposta in "SN" and resposta != " " and resposta != "":
            if resposta == "S":
                continue
            else:
                break
        
        else:
            print("Você digitou uma entrada inválida! Tente novamente.")
            continue

    print("Obrigado por usar nossos serviços!")