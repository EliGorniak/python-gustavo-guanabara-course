# Crie um programa que leia o nome completo de uma pessoa e mostre:

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')

# o nome com todas as letras maiúsculas
print('Seu nome em maiúsculas é {}'.format(nome.upper()))

# o nome com todas minusculas
print('Seu nome em minúsculas é {}'.format(nome.lower()))

# quantas letras ao todo - sem considerar os espaços
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))

# quantas letras tem o primeiro nome
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
