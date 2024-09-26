# Desenvolver um fluxograma e um programa em Python que receba o nome e a
# idade de uma pessoa. Calcule essa idade em meses, dias e horas. Mostre o nome
# # e a idade em meses, dias e horas.

from datetime import datetime

#funçoes

def calcula_idade(dataNascimento):
    dataHoje = datetime.now()
    diferenca = dataHoje - dataNascimento
    idadeEmDias = diferenca.days

#calculos

    anos = idadeEmDias //365
    meses = (idadeEmDias % 365) // 30
    dias = (idadeEmDias % 365) % 30

#singular
    if anos == 1:
        return f"Você tem: {anos} ano de idade, {meses} meses e {dias} dias vividos."
#plural
    else:
        return f"Você tem: {anos} anos de idade, {meses} meses e {dias} dias vividos."

dataNascimento_str = input("Digite sua data de nascimento no formato DD/MM/AAAA: ")
dataNascimento = datetime.strptime(dataNascimento_str, "%d/%m/%Y")

print(calcula_idade(dataNascimento))