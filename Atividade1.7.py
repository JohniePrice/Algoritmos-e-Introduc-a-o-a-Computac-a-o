# Desenvolver um fluxograma e um programa em Python que efetue a
# apresentação do valor da conversão das moedas em dólar, euro e libra de um
# valor lido em real. O algoritmo deverá solicitar a quantidade de reais disponíveis,
# o valor de cada moeda e fazer as referidas cotações.


print("++++++++++++++++++++Conversor de Moedas ++++++++++++++++++++++")
opcao = int(input("Escolha a opção de moeda desejada: \n 1 - Reais \n 2 - Dolar \n 3 - Euro \n 0 - Para sair \n"))

while opcao != 0:

    # opção 1 ----------------------------------------------------------
    if opcao == 1:
        print("Reais \n")
        opcao = int(input("Escolha a moeda para ser convertida: \n1 - Dolar \n2 - Euro \n"))

        if opcao == 1:
            R = float(input("Digite a quantidade de reais: "))
            R_D = (R / 5.44)
            print("\n", R_D, "dólares \n")

        elif opcao == 2:
            R = float(input("Digite a quantidade de reais: "))
            R_E = (R / 6.09)
            print("\n", R_E, "euros \n")

    # Opção 2 ________________________________________________________________
    elif opcao == 2:
        print("Dólar \n")
        opcao = int(input("Escolha a moeda para ser convertida: \n1 - Reais \n2 - Euro \n"))

        if opcao == 1:
            D = float(input("Digite a quantidade de dólares: "))
            D_R = (D * 5.44)
            print("\n", D_R, "reais \n")

        elif opcao == 2:
            D = float(input("Digite a quantidade de dólares: "))
            D_E = (D * 0.89)
            print("\n", D_E, "euros \n")

    # opção 3 ---------------------------------------------------------------------
    elif opcao == 3:
        print("Euro \n")
        opcao = int(input("Escolha a moeda para ser convertida: \n1 - Reais \n2 - Dolar \n"))

        if opcao == 1:
            E = float(input("Digite a quantidade de euros: "))
            E_R = (E * 6.09)
            print("\n", E_R, "reais \n")

        elif opcao == 2:
            E = float(input("Digite a quantidade de euros: "))
            E_D = (E * 1.12)
            print("\n", E_D, "dólares \n")

    opcao = int(input(
        "Escolha a opção de moeda desejada: \n 1 - Reais \n 2 - Dolar \n 3 - Euro \n 0 - Para sair \n"))

print("Programa encerrado.")






R_D = (R * 5.44)
R_E = (R * 6.09)
D_R = (D * 0.18)
D_E = (D * 0.89)
E_D = (E * 1.12)
E_R = (E * 0.16)