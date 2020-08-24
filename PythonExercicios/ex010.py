# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$ 1.00 = R$ 3.27

money = float(input("Quanto dinheiro você tem na sua carteira? R$ "))
dolar = money/3.27
print('Com R${:.2f} você pode comprar US${:.2f}!'.format(money, dolar))
