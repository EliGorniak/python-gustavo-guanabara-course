# Desenvolva um programa que pergunte a distância de uma viagem em KM.
# Calcule o preço da passagem, cobrando R$ 0,50 por KM para viagens de até 200km e R$ 0,45 para viagens mais longas.

distancia = float(input('Qual a distância em KM a ser percorrida na viagem? '))
if distancia <= 200.00:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45
print('O valor da passagem para distância de {} km será de R$ {:.2f}.'.format(distancia, valor))

# usando operador ternário ou condicional inline:
# preço = distancia * 0.50 if distancia <= 200.00 else distancia * 0.45