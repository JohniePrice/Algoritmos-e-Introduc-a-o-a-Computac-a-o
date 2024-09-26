# Desenvolver um fluxograma e um programa em Python para ler uma
# temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. A
# fórmula de conversão é: F= 9*C/ 5 +32, sendo F a temperatura em Fahrenheit e
# C a temperatura em Celsius. Ao final exibir as duas temperaturas.

temp_celsius = float(input("Digite a temperatura em Celsius: "))
F = (9* temp_celsius)/5 +32
print(F, "graus Fahrenheit")