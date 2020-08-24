# Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.

num = int(input('Digite um numero inteiro: '))
dobro = num*2
triplo = num**3
raiz = num**(1/2)
print('1ª opção: Seu número é {}, \nseu dobro é {}, \nseu triplo é {} e \nsua raiz quadrada é {:.2f}.'.format(num, dobro, triplo, raiz))

# 2ª opção:
print('2ª opção: Seu número é {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {:.2f}.'.format(num, (num*2), (num*3), (num**(1/2))))

# 3ª opção para a potência:
print('3ª opção: Seu número é {} e sua raiz quadrada é {:.2f}.'.format(num, pow(num, (1/2))))