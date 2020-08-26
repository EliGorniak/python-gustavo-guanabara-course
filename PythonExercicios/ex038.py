# Escreva um programa que leia 2 números inteiros e compare-os, mostrando na tela uma das seguintes mensagens:
# O primeiro valor é MAIOR
# O segundo valor é MAIOR
# Não existe valor maior, os dois são iguais

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if num1 > num2:
    print('O PRIMEIRO número é maior que o segundo.')
elif num2 > num1:
    print('O SEGUNDO número é maior que o primeiro.')
else:
    print('Não existe valor maior, ambos são iguais.')
