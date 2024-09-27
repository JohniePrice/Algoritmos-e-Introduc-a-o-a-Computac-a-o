# Desenvolver um fluxograma e um programa em Python que leia o número de
# lados de um polígono regular e a medida do lado (em cm). Calcular e imprimir o
# seguinte:
# • Se o número de lados for igual a 3 escrever TRIÂNGULO e o valor da área
# • Se o número de lados for igual a 4 escrever QUADRADO e o valor da sua área.
# • Se o número de lados for igual a 5 escrever PENTÁGONO.
# • Se número de lados for inferior a 3 escrever NÃO É UM POLÍGONO.
# • Se número de lados for superior a 5 escrever POLÍGONO NÃO IDENTIFICADO.

import math


def calcular_area_poligono(lados, medida):
    # Fórmula da área de um polígono regular
    area = (1 / 4) * lados * (medida ** 2) * (1 / math.tan(math.pi / lados))
    return area


lados = int(input("Digite o número de lados: "))
medida = float(input("Digite a medida de cada lado: "))
unidade_utilizada = int(input("Digite 1 para mm \n 2 para cm \n 3 para km: "))

if unidade_utilizada == 1:
    unidade = "mm"
elif unidade_utilizada == 2:
    unidade = "cm"
elif unidade_utilizada == 3:
    unidade = "km"
else:
    print("Unidade não reconhecida.")
    exit()

if lados < 3:
    print("Não é um polígono")

elif lados == 3:
    print("TRIÂNGULO")
    area = calcular_area_poligono(lados, medida)
    print(f"A área do Triângulo é: {area:.2f} {unidade} quadrados")

elif lados == 4:
    print("QUADRADO")
    area = calcular_area_poligono(lados, medida)
    print(f"A área do Quadrado é: {area:.2f} {unidade} quadrados")

elif lados == 5:
    print("PENTÁGONO")
    area = calcular_area_poligono(lados, medida)
    print(f"A área do Pentágono é: {area:.2f} {unidade} quadrados")

elif lados > 5:
    print("Polígono não identificado")
else:
    print("Número de lados inválido.")




