# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a média.

aluno = input("Digite o nome do aluno: ")
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2
print('A média do {} é {:.1f}.'.format(aluno, media))