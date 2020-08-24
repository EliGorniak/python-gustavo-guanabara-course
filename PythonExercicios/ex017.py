# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

# 1º opção: sem utilizar a biblioteca Math
co = float(input('Indique o comprimento do cateto oposto: '))
ca = float(input('Indique o comprimento do cateto adjacente: '))
hip = (co**2 + ca**2) **(1/2)
print('O valor da hipotenusa é {:.2f}'.format(hip))


# 2ª opção: importação de um método específico dentro da biblioteca Math
import math
cop = float(input('Indique o comprimento do cateto oposto: '))
cad = float(input('Indique o comprimento do cateto adjacente: '))
hipo = math.hypot(cop, cad)
print('O valor da hipotenusa é {:.2f}'.format(hipo))


