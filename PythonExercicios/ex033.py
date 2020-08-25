# Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.

n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))
n3 = float(input('Digite um número: '))

# achando o menor numero:
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# achando o maior número:
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3

print('O menor numero digitado é {}.'.format(int(menor)))
print('O maior número digitado é {}.'.format(int(maior)))
