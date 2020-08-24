# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

# 1ª opção: com importação da biblioteca Math inteira
import math
angulo = float(input("Digite o ângulo: "))
s = math.sin(math.radians(angulo))
c = math.cos(math.radians(angulo))
t = math.tan(math.radians(angulo))
print('O SENO de {} é {:.2f}'.format(angulo, s))
print('O COSSENO de {} é {:.2f}'.format(angulo, c))
print('A TANGENTE de {} é {:.2f}'.format(angulo, t))

# 2ª opção: com importação de métodos específicos dentro da biblioteca Math
from math import radians, sin, cos, tan
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print('O SENO de {} é {:.2f}'.format(angulo, sen))
print('O COSSENO de {} é {:.2f}'.format(angulo, cos))
print('A TANGENTE de {} é {:.2f}'.format(angulo, tan))



