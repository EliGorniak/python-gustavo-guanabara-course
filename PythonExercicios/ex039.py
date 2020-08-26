# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# a) se ele ainda vai se alistar ao serviço militar
# b) se é a hora de se alistar
# c) se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date
ano = int(input('Digite o ano do seu nascimento: '))
idadealistamento = 18
idade = date.today().year - ano
print('Sua idade: {}.'.format(idade))
if idade < 18:
    print('Você tem apenas {} anos, portanto, faltam {} anos para você se alistar.'.format(idade, 18 - idade))
elif idade == 18:
    print('Você já tem {} anos, portanto, está na hora de se alistar!'.format(idadealistamento))
else:
    print('Você tem {} anos de idade, portanto, já se passaram {} anos do seu alistamento!'.format(idade, idade - 18))
