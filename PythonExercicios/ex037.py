# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# -1 para binário
# -2 para octal
# -3 para hexadecimal

cores = {# cores em negrito
        'limpa': '\033[m',
        'branconegrito': '\033[1;30m',
        'vermelhonegrito': '\033[1;31m',
        'verdenegrito': '\033[1;32m',
        'amarelonegrito': '\033[1;33m',
        'azulnegrito': '\033[1;34m',
        'roxonegrito': '\033[1;35m',
        'cianonegrito': '\033[1;36m',
        'cinzanegrito': '\033[37m',
        }

num = int(input('Digite um número inteiro: '))
print('Opções para conversão:')
print('Digite 1 para BINÁRIO')
print('Digite 2 para OCTAL')
print('Digite 3 para HEXADECIMAL')
escolha = int(input('Digite sua opção: '))
if escolha == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format(num, bin(num) [2:])) # [2:] cortou o 0b
elif escolha == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(num, oct(num) [2:])) # [2:] cortou o 0o
elif escolha == 3:
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(num, hex(num) [2:])) # [2:] cortou o Ox
else:
    print('Opção inválida. Tente novamente.')
print('-.-'*30)
print(' {}Resumindo: {} será {} em BINÁRIO, {} em OCTAL e {} em HEXADECIMAL{}.'.format(cores['verdenegrito'], num, bin(num), oct(num), hex(num), cores['limpa']))
print('-.-'*30)
