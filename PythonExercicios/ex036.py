# Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

cores = {# cores em negrito
        'limpa': '\033[m',
        'branconegrito': '\033[1;30m',
        'vermelhonegrito': '\033[1;31m',
        'verdenegrito': '\033[1;32m',
        'amarelonegrito': '\033[1;33m',
        'azulnegrito': '\033[1;34m',
        'roxonegrito': '\033[1;35m',
        'cianonegrito': '\033[1;36m',
        'cinzanegrito': '\033[37m',
        }

valorDaCasa = float(input('Valor da casa: '))
salario = float(input('Seu salário mensal: '))
prazo = float(input('Prazo em anos para financiamento: '))
prestação = valorDaCasa / (prazo * 12)
print('O valor mensal da prestação será de R$ {:.2f}.'.format(prestação))
print('30% do seu salário corresponde a R$ {:.2f}.'.format(salario * 0.30))
if prestação <= (salario * 0.30):
    print('Parabéns! Seu empréstimo bancário foi {}APROVADO{} para uma prestação mensal de R$ {:.2f}.'.format(cores['azulnegrito'], cores['limpa'], prestação))
else:
    print('Seu empréstimo foi {}NEGADO{} pois o valor da prestação mensal excede 30% do seu salário.'.format(cores['vermelhonegrito'], cores['limpa']))
