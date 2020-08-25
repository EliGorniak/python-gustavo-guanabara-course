# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada km acima do limite.

velocidade = float(input('Escreva a velocidade do carro em km/h: '))
if velocidade > 80.00:
    multa = (velocidade - 80.00) * 7.00
    print('Sua velocidade estava acima do limite de 80km/h e você será multado em R$ {:.2f}!'.format(multa))
    print('Lembre-se sempre de dirigir com segurança!')
else:
    print('Tenha um bom dia e dirija com segurança!')


