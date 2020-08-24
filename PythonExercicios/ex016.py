# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira.
# Ex: Digite um número: 6.127. O número 6.127 tem a parte inteira 6.

# 1ª opção: importação de um método específico dentro da biblioteca Math
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, trunc(num)))

# 2º opção: sem utilizar a biblioteca Math
num1 = float(input('Digite um valor novamente: '))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num1, int(num1)))