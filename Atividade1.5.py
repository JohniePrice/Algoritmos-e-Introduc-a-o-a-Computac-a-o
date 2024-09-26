# Desenvolver um fluxograma e um programa em Python que leia o nome de um
# vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em
# dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas
# vendas efetuadas, informar o seu nome, o salário fixo, o valor da comissão e
# salário no final do mês.

nome_vendedor = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salario fixo: "))
vendas_efetuadas = float(input("Digite o total de vendas efetuadas: "))
comissao = float(vendas_efetuadas * 0.15)
salario_no_final_mes = float(salario_fixo + comissao)
print("O "+ nome_vendedor +":"+ "tem o salario fixo de: "+str(salario_fixo)+ "e a comissao de: "+str(comissao)+ "e o salario no final do mes de: "+str(salario_no_final_mes)+ "reais")