# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta tinta pinta uma área de 2m2.

largura = float(input("Digite a largura da parede em metros: "))
altura = float(input('Digite a altura da parede em metros: '))
areaparede = (largura*altura)
tinta = areaparede/2
print('A parede tem {:.2f}m².'.format(areaparede))
print('Serão necessários {:.1f} litros de tinta para pintar a parede.'.format(tinta))
