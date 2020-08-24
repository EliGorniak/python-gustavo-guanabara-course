# Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada.

num = int(input('Digite um número: '))

def tabuada(x):
    for valor in range(1, 11):
        print('{0} x {1:2} = {2:2}'.format(x, valor, x*valor))

tabuada(num)



