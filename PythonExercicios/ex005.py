# Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor

num = int(input('Digite um numero inteiro: '))
numantecessor = num - 1
numsucessor = num + 1
print('O número é {}, seu antecessor é {}, e seu sucessor é {}.'.format(num, numantecessor, numsucessor))
print('O núermo é {}, seu antecessor é {}, e seu sucessor é {}.'.format(num, (num-1), (num+1))) # caso não precise declarar e usar as variaveis antecessor e sucessor posteriormente.