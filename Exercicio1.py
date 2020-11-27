# Faça um Programa que pergunte quanto você ganha por hora
# e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são
# descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
# para o sindicato, faça um programa que nos dê:

#     salário bruto.
#     quanto pagou ao INSS.
#     quanto pagou ao sindicato.
#     o salário líquido.
#     calcule os descontos e o salário líquido, conforme a tabela abaixo: 
#     + Salário Bruto : R$
#     - IR (11%) : R$
#     - INSS (8%) : R$
#     - Sindicato ( 5%) : R$
#     = Salário Liquido : R$

def limpar_tela():
    from os import name, system
    
    if name == 'nt': 
        system('cls') 
    else: 
        system('clear')      


def main():
    from time import sleep
    
    limpar_tela()
    taxa_inss = 0.08
    taxa_imp_renda = 0.11
    taxa_sindicato = 0.05
    msg = "Calculador de desconto salarial"
    print("="*60)
    print(f"{msg:^60}")
    print("="*60)
    print("Bem vindo ao calculador de descontos de funcionário.\n"
          "Digite abaixo as informações solicitadas do\nfuncionário para "
          "ver o desconto salarial.\n")
    salario_hora = float(input("Salário por hora: "))
    horas = float(input("Horas trabalhadas no mês: "))
    

    salario_bruto = round(salario_hora * horas, 2)
    contribuicao_inss = salario_bruto * taxa_inss
    contribuicao_imp_renda = salario_bruto * taxa_imp_renda
    contribuicao_sindicato = salario_bruto * taxa_sindicato
    salario_liquido = (salario_bruto
                       - contribuicao_imp_renda
                       - contribuicao_inss
                       - contribuicao_sindicato)

    # dessa forma fica muito bom visualmente
    limpar_tela()
    print("Calculando descontos! Aguarde...")
    sleep(2)
    limpar_tela()
    msg = "Tabela de desconto do funcionário"
    print("="*60)
    print(f"{msg:^50}")
    print("="*60)
    # talvez usar um \t deixe mais claro a ideia da margem
    print(f"\n{'':^10}+ Salário Bruto: R${salario_bruto:<40}")
    print(f"{'':^10}- IR {int(taxa_imp_renda*100)}%: "
          f"R${contribuicao_imp_renda:<40}")
    print(f"{'':^10}- INSS {int(taxa_inss*100)}%: "
          f"R${contribuicao_inss:<40}")
    print(f"{'':^10}- Sindicato {int(taxa_sindicato*100)}%: "
          f"R${contribuicao_sindicato:<40}")
    print(f"{'':^10}= Salário Líquido: R${round(salario_liquido, 2):<40}\n")
    print("-"*50)
    

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
        