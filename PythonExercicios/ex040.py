# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# a) média abaixo de 5.0: REPROVADO
# b) média entre 5.0 e 6.9: RECUPERAÇÃO
# c) média igual a 7.0 ou superior: APROVADO

nome = str(input('Digite o nome do aluno: '))
nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2)/2
if media < 5:
    print('{}, sua média final é {}, você está REPROVADO!'.format(nome, media))
elif 5 <= media <= 6.9:
    print('{}, sua média final é {}, você está em RECUPERAÇÃO!'.format(nome, media))
elif media > 7.0:
    print('{}, sua média final é {}, você está APROVADO!'.format(nome, media))
