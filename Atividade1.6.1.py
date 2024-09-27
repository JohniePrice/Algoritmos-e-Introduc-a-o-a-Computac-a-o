# Desenvolver um fluxograma e um programa em Python para ler uma
# temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. A
# fórmula de conversão é: F= 9*C/ 5 +32, sendo F a temperatura em Fahrenheit e
# C a temperatura em Celsius. Ao final exibir as duas temperaturas.

print("+++++++++++++++++Conversor de temperatura+++++++++++++++++++ \n")
opcao = int(input("escolha a opção de temperatura desejada: \n 1 - Celsius \n 2 - Fahrenheit \n 3 - Kelvin \n 0 - Para sair \n"))

while opcao != 0:

#opção 1 ----------------------------------------------------------
    if opcao == 1:
        print("Celsius \n")
        opcao = int(input("Escolha a temperatura para ser convertida: \n1 - Kelvin \n2 - Fahrenheit \n"))

        if opcao == 1:
            temp = float(input("Digite a temperatura: "))
            K = temp + 273.15
            print("\n", K, "graus Kelvin \n")

        elif opcao == 2:
            temp = float(input("Digite a temperatura: "))
            F = (9 * temp) / 5 + 32
            print("\n", F, "graus Fahrenheit \n")

#opção 2 ----------------------------------------------------------

    elif opcao == 2:
        print("Fahrenheit \n")
        opcao = int(input("Escolha a temperatura para ser convertida: \n1 - Kelvin \n2 - Celsius \n"))

        if opcao == 1:
            temp = float(input("Digite a temperatura: "))
            K = (temp - 32) * (5 / 9) + 273.15
            print("\n", K, "graus Kelvin \n")

        elif opcao == 2:
            temp = float(input("Digite a temperatura: "))
            C = (temp - 32) * (5 / 9)
            print("\n", C, "graus Celsius \n")

#opcao 3 -------------------------------------------------------

    elif opcao == 3:
        print("Kelvin \n")
        opcao = int(input("Escolha a temperatura para ser convertida: \n1 - Fahrenheit \n2 - Celsius \n"))

        if opcao == 1:
            temp = float(input("Digite a temperatura: "))
            F = (temp - 273.15) * (9 / 5) + 32
            print("\n", F, "graus Fahrenheit \n")

        elif opcao == 2:
            temp = float(input("Digite a temperatura: "))
            C = temp - 273.15
            print("\n", C, "graus Celsius \n")

    opcao = int(input(
        "Escolha a opção de temperatura desejada: \n 1 - Celsius \n 2 - Fahrenheit \n 3 - Kelvin \n 0 - Para sair \n"))

print("Programa encerrado.")




