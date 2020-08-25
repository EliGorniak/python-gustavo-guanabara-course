# Crie um programa que leia um número inteiro na tela se ela é par ou ímpar.

num = int(input('Escreva um número inteiro: '))
resto = num % 2
if resto == 0:
    print('O número {} é par!'.format(resto))
else:
    print('O número {} é ímpar!'.format(resto))
