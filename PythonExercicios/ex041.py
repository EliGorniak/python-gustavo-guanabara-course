# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostra sua categoria, de acordo com a sua idade
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 25 anos: SÊNIOR
# Acima: MASTER

from datetime import date
ano = int(input('Digite o ano do seu nascimento: '))
idade = date.today().year - ano
print('Sua idade: {}.'.format(idade))
if idade <= 9:
    print('O atleta está na categoria MIRIM.')
elif idade <= 14:
    print('O atleta está na categoria INFANTIL.')
elif idade <= 19:
    print('O atleta está na categoria JUNIOR.')
elif idade <= 25:
    print('O atleta está na categoria SÊNIOR.')
else:
    print('O atleta está na categoria MASTER.')