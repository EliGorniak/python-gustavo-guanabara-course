# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

# usando o método random (aleatório)
import random
aluno1 = str(input('O primeiro aluno é: '))
aluno2 = str(input('O segundo aluno é: '))
aluno3 = str(input('O terceiro aluno é: '))
aluno4 = str(input('O quarto aluno é: '))
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print('O aluno sorteado é {}!'.format(escolhido))

