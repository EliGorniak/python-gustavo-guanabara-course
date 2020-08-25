# operadores aritméticos e tipos:

# crie um programa que leia dois numeros e mostre a soma entre eles
n1 = int((input('Digite um valor: ')))
n2 = int((input('Digite outro valor: ')))
soma = n1 + n2
print('A soma entre {} e {} é: {}!'.format(n1, n2, soma))


# crie um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possiveis sobre ele
n = (input('Digite um valor: '))
print(n.isalnum())
print(n.isdecimal())
print(n.isalpha())
