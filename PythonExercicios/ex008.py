# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

valor = float(input("Digite a distância em metros: "))
centimetros = valor * 100
milimetros = valor * 1000
print('=' * 50)
print('A distância de {}m equivale a {:.0f}cm e {:.0f}mm.'.format(valor, centimetros, milimetros))
print('=' * 50)