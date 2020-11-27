# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

#     Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#     comprar apenas latas de 18 litros;
#     comprar apenas galões de 3,6 litros;
#     misturar latas e galões, de forma que o desperdício de tinta seja menor.
#     Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
# 

def limpar_tela():
    from os import name, system
    
    if name == 'nt': 
        system('cls') 
    else: 
        system('clear') 


def main():
    from time import sleep
    
    # uso do round que nós não vimos em aula para arredondar
    cobertura_tinta = round(1/6, 10)
    margem_erro = 1.10
    valor_18 = 80
    valor_3_6 = 25
    msg = "Calculador de latas de tinta!"
    print("="*60)
    print(f"{msg:^60}")
    print("="*60)
    print("Bem vindo ao calculador de latas de tinta Pythonil!\n"
          "Entre com as informações abaixo para calcular\n"
          "o total de latas de tinta necessários.")
    
    area_pintar = float(input(u"Digite a área a ser pintada [m²]:\n"))
    limpar_tela()
    print("Calculando! Aguarde...")
    sleep(2)
    limpar_tela()
    total_litros = area_pintar * cobertura_tinta
    # arredondar o número de casas decimais
    print(total_litros)
    total_latas18 = int((total_litros * margem_erro)// 18)
    total_latas3_6 = int((total_litros * margem_erro) // 3.6)
    
    latas_18_otimizado = total_latas18
    latas_3_6_otimizado = int(((total_litros * margem_erro) % 18) // 3.6)
    
    if (total_litros % 18) % 3.6 > 0:
        latas_3_6_otimizado += 1
      
    if total_litros % 18 > 0:
        total_latas18 += 1
    
    if total_litros % 3.6 > 0:
        total_latas3_6 += 1
    
    
    print("Calculando descontos! Aguarde...")
    msg = "Opções de compras"
    print("="*60)
    print(f"{msg:^50}")
    print("="*60)
    # não compreendi muito bem a usabilidade do '<2'
    print(f"\n{'':^10}Latas de 18L: {total_latas18:<2} - R${valor_18 * total_latas18}")
    print(f"{'':^10}Latas de 3,6L: {total_latas3_6:<2} - R${valor_3_6 * total_latas3_6}")
    print(f"\n{'':^10}Otimizado: {latas_18_otimizado:<2} latas de 18L")
    print(f"{'':^10}           {latas_3_6_otimizado:<2} latas de 3,6L\n"
          f"                     R${valor_18*latas_18_otimizado + valor_3_6*latas_3_6_otimizado}\n")
    
    
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