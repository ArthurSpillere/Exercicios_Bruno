# Faça um Programa que peça os 3 lados de um triângulo.
# O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

def limpar_tela():
    from os import name, system
    
    if name == 'nt': 
        system('cls') 
    else: 
        system('clear')


def main():
    msg = "Verificador e classificador de triângulos!"
    print("="*60)
    print(f"{msg:^60}")
    print("="*60)
    lado_a = float(input("\nDigite o primeiro lado do triangulo:\n"))
    lado_b = float(input("Digite o segundo lado do triangulo:\n"))
    lado_c = float(input("Digite o terceiro lado do triangulo:\n"))

    if (lado_a > lado_b + lado_c
        or lado_b > lado_a + lado_c
        or lado_c > lado_a + lado_b):
        
        print("\nEstas dimensões não formam um triângulo!")

    else:
        
        if lado_a == lado_b and lado_b == lado_c:
            print("\nEstas dimensões formam um triângulo equilátero!\n"
                "Todos os seus lados são iguais.\n")
        
        elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
            print("\nEstas dimensões formam um triângulo isósceles!\n"
                "Dois dos seus lados são iguais.\n")
        
        else:
            print("\nEstas dimensões formam um triângulo escaleno!\n"
                "Nenhum dos seus lados são iguais.\n")


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