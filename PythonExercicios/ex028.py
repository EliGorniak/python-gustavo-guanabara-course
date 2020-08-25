# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário descobrir qual foi o numero escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
pc = randint(0, 5)
print('+...+...' * 12)
print('Olá, sou o computador e vou pensar num número entre 0 e 5 e você vai tentar adivinhá-lo ok!')
print('+...+...' * 12)
user = int(input('Adivinhe um valor entre 0 e 5: '))
print('Ok, processando...')
sleep(2)
if user == pc:
    print('Ok, você acertou! Você ganhou!')
else:
    print('Ah não, você errou, eu pensei no número {}. Tente outra vez!'.format(pc))