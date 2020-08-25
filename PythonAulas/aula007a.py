# OPERADORES ARITMÉTICOS EM PYTHON

'''
# função print:
nome = input('Qual é o seu nome?')
print('Prazer em te conhecer {}!'.format(nome))
print('Prazer em te conhecer {:20}!'.format(nome)) # acrescenta 20 espaços depois do nome
print('Prazer em te conhecer {:>20}!'.format(nome)) # alinha o conteudo à direita
print('Prazer em te conhecer {:<20}!'.format(nome)) # alinha o conteudo à esquerda
print('Prazer em te conhecer {:^20}!'.format(nome)) # centraliza o conteudo entre 20 espaços
print('Prazer em te conhecer {:=^20}!'.format(nome)) # centraliza o conteudo entre 20 sinais de =
'''

# operadores:
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {}, a divisão é {:.3f}, a divisão inteira é {}, a potencia é {}'.format(s, m, d, di, e))
# {:3.} transforma o produto da divisão em apenas 3 casas decimais
# para quebrar a linha inserir \n - nova linha
# para juntar 2 linhas inserir end=' ' ou end=' --- ' ou o sinal ou simbolo que quiser
