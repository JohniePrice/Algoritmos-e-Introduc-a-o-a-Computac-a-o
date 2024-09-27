# Desenvolver um fluxograma e um programa em Python que leia 3 valores A, B, C
# e exiba se é um triângulo Isóscele, Equilátero, Escaleno ou se não é triângulo.
# • É triângulo quando cada um dos lados for menor que a soma dos outros dois;
# • É triângulo Equilátero quando todos os lados forem iguais;
# • É triângulo Escaleno quando todos os lados forem diferentes;
# • É triângulo Isósceles quando dois lados forem iguais e um diferente.

valor_a = float(input("Digite o valor de A: "))
valor_b = float(input("Digite o valor de B: "))
valor_c = float(input("Digite o valor de C: "))

if valor_a < valor_b + valor_c and valor_b < valor_a + valor_c and valor_c < valor_a + valor_b:
    print("é um triangulo")
    if valor_a == valor_b == valor_c:
        print("é um triandulo equilatero")
    elif valor_a != valor_b != valor_c != valor_a:
        print("é um triangulo escaleno")
    elif valor_a == valor_b or valor_a == valor_c or valor_b == valor_c:
        print("é um triangulo isosceles")
else:
    print("não é um triangulo")

