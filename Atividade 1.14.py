# Desenvolver um fluxograma e um programa em Python que leia o nome e as três
# notas obtidas por um aluno durante o semestre. Calcular a sua média
# (aritmética), informar o nome e sua menção aprovado (media >= 7), Reprovado
# (media <= 5) e Recuperação (media entre 5.1 a 6.9).

nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1+nota2+nota3)/3

if media <= 5:
    print(f"O aluno: {nome} está reprovado. nota: {media}")
elif media >= 5.1 and media <= 6.9:
    print(f"O aluno: {nome} esta de recuperação. nota: {media}" )
elif media >= 7:
    print(f"O aluno: {nome} está aprovado. nota: {media}")