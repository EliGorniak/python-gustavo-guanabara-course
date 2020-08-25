# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
# Para salários inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o valor do seu salário: R$ '))
if salario <= 1250.00:
    aumento = (salario * 0.15) + salario
if salario > 1250.00:
    aumento = (salario * 0.10) + salario

print('Seu salário reajustado será de R$ {:.2f}'.format(aumento))