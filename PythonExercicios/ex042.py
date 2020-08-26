# Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais
# ESCALENO: todos os lados diferentes

# DICA: 3 lados formam um triângulo quando a soma de quaisquer 2 lados for maior que o terceiro.

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if (r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1):
    if r1 == r2 == r3:
        print('Estes valores formarão um triângulo EQUILÁTERO!')
    if r1 != r2 != r3 != r1:
        print('Estes valores formarão um triângulo ESCALENO!')
    else:
        print('Estes valores formarão um triângulo ISÓSCELES!')
else:
    print('Estes valores não poderão formar um triângulo!')
