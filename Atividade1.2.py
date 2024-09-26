
# Desenvolver um fluxograma e um programa em Python para determinar o
# consumo médio de um automóvel sendo fornecida a distância total percorrida
# pelo automóvel e o total de combustível gasto.
# CONSUMO=DITANCIA_PERCORRIDA/COMBUSTIVEL_GASTO

distancia_percorrida = float(input("Digite a distancia percorrida: "))
combustivel_gasto = float(input("Digite a quantidade de combustivel gasto: "))
consumo = distancia_percorrida / combustivel_gasto
print("O consumo foi de: ", consumo, " km/l")