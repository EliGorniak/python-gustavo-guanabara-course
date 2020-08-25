# Faça um programa que elia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
# Ex: Ana Maria de Souza
# primeiro: Ana
# último: Souza

nome = str(input('Digite seu nome completo: ')).strip()
nome2 = nome.split() # cria uma lista
print(nome2)
print(len(nome2))
print('Primeiro nome: {}'.format(nome2[0]))
print('Segundo nome: {}'.format(nome2[len(nome2)-1])) # para pegar o último item da lista
