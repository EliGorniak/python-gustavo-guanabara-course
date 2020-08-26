# Cores no Python
'''
\033[0;30;41m
\033[4;33;44m
\033[1;35;43m
\033[30;42m
\033[m # cor padrão do terminal
\033[7;30 # inversão do fundo preto e letra branca
'''

print('\33[1;30;41mOlá mundo!\033[m')
a = 3
b = 5
print('Os valores são \033[1;32m{}\033[m e \033[1;31m{}\033[m!!!'.format(a, b))

nome = 'Daniela'
print('Olá, muito prazer em conhecê-la, {}{}{}!'.format('\033[4;34m', nome, '\033[m'))

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}
print('Olá, muito prazer em conhecê-la, {}{}{}!'.format(cores['amarelo'], nome, cores['limpa']))
