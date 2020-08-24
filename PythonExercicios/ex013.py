# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

salario = float(input('Digite o valor do salario: R$ '))
aumento = salario+(salario*0.15)
print('O novo salario do funcionario é de R$ {:.2f}.'.format(aumento))