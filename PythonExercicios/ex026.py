# Faça um programa que leia uma frase pelo teclado e mostre:

frase = str(input("Digite uma frase: ")).upper().strip()

#para frases com acentuação, usar replace:
frase2 = frase.replace('Á', 'A').replace('Ã', 'A').replace('À', 'A')

# quantas vezes aparece a letra "A"
print('A letra A aparece {} vezes na frase.'.format(frase2.count('A')))

# em que posição ela aparece a primeira vez
print('A primeira letra A apareceu na posição {}'.format(frase2.find('A')+1))

# em que posição ela aparece a última vez
print('A última letra A apareceu na posição {}'.format(frase2.rfind('A')+1))