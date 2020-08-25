# Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo.

# DICA: 3 lados formam um triângulo quando a soma de quaisquer 2 lados for maior que o terceiro.

r1 = float(input('Digite um valor: '))
r2 = float(input('Digite um valor: '))
r3 = float(input('Digite um valor: '))

if (r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1):
    print('Estes valores poderão formar um triângulo!')
else:
    print('Estes valores não poderão formar um triângulo!')
