# crie um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possiveis sobre ele

n = (input('Digite um valor: '))
print('O tipo primitivo desse valor é ', type(n))
print('Só tem espaços? ', n.isspace())
print('É um número? ', n.isnumeric())
print('É alfanumérico?', n.isalnum())
print('Está em minúsculas?', n.islower())
print('Está em maiúsculas?', n.isupper())
print('Está capitalizada?', n.istitle())

