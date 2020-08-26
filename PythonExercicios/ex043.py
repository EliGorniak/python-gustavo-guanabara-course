# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: ABAIXO DO PESO
# Entre 18.5 e 25: PESO IDEAL
# De 25 até 30: SOBREPESO
# De 30 até 40: OBESIDADE
# Acima de 40: OBESIDADE MÓRBIDA

peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em m: '))
imc = peso/altura**2

if imc < 18.5:
    print('Seu imc é {:.1f}, portanto, você está ABAIXO DO PESO.'.format(imc))
elif imc < 25:
    print('Seu imc é {:.1f}, portanto, você está no PESO IDEAL.'.format(imc))
elif imc < 30:
    print('Seu imc é {:.1f}, portanto, você está em SOBREPESO.'.format(imc))
elif imc < 40:
    print('Seu imc é {:.1f}, portanto, você está com OBESIDADE.'.format(imc))
else:
    print('Seu imc é {:.1f}, portanto, você está com OBESIDADE MÓRBIDA.'.format(imc))
