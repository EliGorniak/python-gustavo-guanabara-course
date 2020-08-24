# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por KM rodado:

km = float(input('Quantos kilometros você percorreu? '))
dias = int(input('Por quantos dias ele foi alugado? '))
custokmrodado = 0.15
custoaluguel = 60
totalapagar = (km*custokmrodado) + (dias*custoaluguel)
print('O valor a pagar é de R$ {:0.2f}'.format(totalapagar))


