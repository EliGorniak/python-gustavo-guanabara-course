# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

# usando módulo random.shuffle para embaralhar a lista e mostrar essa lista nesta nova ordem:
from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
# random.shuffle(lista) sem importar unicamente o metodo shuffle

shuffle(lista) #importando apenas o método shuffle
print('A ordem de apresentação dos trabalhos será: {}.', format(lista))

