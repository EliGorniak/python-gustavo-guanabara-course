# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep
import emoji

itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA 
[ 1 ] PAPEL 
[ 2 ] TESOURA ''')
jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)

print('+...+...' * 5)
print('O computador escolheu {}.'.format(itens[pc]))
print('Você escolheu {}.'.format(itens[jogador]))
print('+...+...' * 5)

print(emoji.emojize(':fist:', use_aliases=True), emoji.emojize(':hand:', use_aliases=True), emoji.emojize(':v:', use_aliases=True))
if pc == 0: # computador jogou PEDRA
    if jogador == 0:
        print('Deu empate. Tente de novo!')
    elif jogador == 1:
        print('Você ganhou!')
    elif jogador == 2:
        print('O computador ganhou!')
    else:
        print('Jogada inválida. Tente novamente.')

elif pc == 1: # computador jogou PAPEL
    if jogador == 0:
        print('O computador ganhou!')
    elif jogador == 1:
        print('Deu empate. Tente de novo!')
    elif jogador == 2:
        print('Você ganhou!')
    else:
        print('Jogada inválida. Tente novamente.')

elif pc == 2: # computador jogou TESOURA
    if jogador == 0:
        print('Você ganhou!')
    elif jogador == 1:
        print('O computador ganhou!')
    elif jogador == 2:
        print('Deu empate. Tente de novo!')
    else:
        print('Jogada inválida. Tente novamente.')












