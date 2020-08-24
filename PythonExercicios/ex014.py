# Crie um programa que converta a temperatura de Celsius para Fahrenheit:

c = float(input('Informe a temperatura em Celsius: '))
f = ((9 * c) /5) + 32
print(('A temperatura de {} ºC corresponde a {} ºF.'.format(c, f)))

# Crie um programa que converta a temperatura de Fahrenheit para Celsius:

far = float(input('Informe a temperatura em Fahrenheit: '))
cel = (far-32)/1.8
print(('A temperatura de {} ºC corresponde a {:.1f} ºF.'.format(far, cel)))