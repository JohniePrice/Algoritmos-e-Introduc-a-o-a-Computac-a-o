# Desenvolver um fluxograma e um programa em Python que leia a altura e peso
# de uma pessoa e calcule o IMC. O índice de massa corpórea (IMC) pode ser
# obtido pela fórmula: peso / (altura2
# ).
# • imc < 18.5, escrever “MAGRO”,
# • imc >= 18.5 e imc < 25, escrever “NORMA!”
# • imc >= 25 e imc < 30, escrever "SOBREPESO”
# • imc >=30 e imc < 40, escrever “OBESO!”
# • imc >= 30, escrever "OBESO MORBIDO”

print("+++++++++++++++++++++Calculadora de IMC++++++++++++++++++++")
peso = float(input("Qual seu peso? "))
altura = float(input("Qual sua altura? "))

def Calculo_Imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

if Calculo_Imc(peso, altura) < 18.5:
    print(" magro ")
elif Calculo_Imc(peso, altura) >= 18.5 and Calculo_Imc(peso, altura) < 25:
    print(" norme ")
elif Calculo_Imc(peso, altura) >= 25 and Calculo_Imc(peso, altura) < 30:
    print(" sobrepeso ")
elif Calculo_Imc(peso, altura) >= 30 and Calculo_Imc(peso, altura) < 40:
    print(" obeso ")
elif Calculo_Imc(peso, altura) >= 40:
    print(" obeso morbido ")


