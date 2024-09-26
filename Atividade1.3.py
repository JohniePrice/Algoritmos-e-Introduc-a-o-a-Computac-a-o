# Desenvolver um fluxograma e um programa em Python que leia o nome de um
# aluno e as notas das três provas que ele obteve no semestre. No final, informar o
# nome do aluno e a sua média (aritmética).
from tokenize import String

nomeAluno = (input("Digite o nome do aluno: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
mediaNota = float(nota1+nota2+nota3) / 3
print("O "+ nomeAluno +":"+ "tem a media de: "+str(mediaNota))