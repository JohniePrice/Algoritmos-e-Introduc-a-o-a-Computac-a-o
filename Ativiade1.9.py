# Desenvolver um fluxograma e um programa em Python que receba o preço de
# custo de um produto e mostre o valor de venda. Sabe-se que o preço de custo
# receberá um acréscimo de acordo com um percentual informado pelo usuário.

produto = float(input("Digite o valor do produto:"))
percentual = float(input("Digite o percentual de aumento:"))
print("valor final do produto"+produto + (produto * percentual / 100))