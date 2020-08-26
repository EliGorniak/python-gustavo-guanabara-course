# Condicionais

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('A sua média foi {:.1f}.'.format(media))
if media >= 6.0:
    print('Sua média foi boa! Parabéns!')
else:
    print('Estude mais ok!')

# outra forma de escrever mais compactado é:
# print('Parabéns!' if media >= 6 else 'Estude mais!')