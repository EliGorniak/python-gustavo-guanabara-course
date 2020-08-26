# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

cores = {'limpa': '\033[m',
         'vermelhonegrito': '\033[1;31m',
         'azulnegrito': '\033[1;34m',
         'amarelonegrito': '\033[1;33m',
         'branconegrito': '\033[1;30m',
         'roxonegrito': '\033[1;35m',
         'verdenegrito': '\033[1;32m',
         'cianonegrito': '\033[1;36m'}

valor = float(input('Digite o valor do produto: R$ '))
print('Opções para pagamento:')
print('Digite {}1{} para pagamento à vista usando dinheiro ou cheque'.format(cores['vermelhonegrito'], cores['limpa']))
print('Digite {}2{} para pagamento à vista no cartão'.format(cores['azulnegrito'], cores['limpa']))
print('Digite {}3{} para pagar em até 2x no cartão'.format(cores['roxonegrito'], cores['limpa']))
print('Digite {}4{} para pagar em 3x ou mais no cartão'.format(cores['verdenegrito'], cores['limpa']))
escolha = str(input('Digite o número correspondente à condição de pagamento escolhida: '))
valorEscolha1 = valor - (valor * 0.10)
valorEscolha2 = valor - (valor * 0.05)
valorEscolha3 = valor
valorEscolha4 = valor + (valor * 0.20)
if escolha == '1':
    print('O preço final será de {}R$ {:.2f}{}.'.format(cores['vermelhonegrito'], valorEscolha1, cores['limpa']))
elif escolha == '2':
    print('O preço final será de {}R$ {:.2f}{}.'.format(cores['azulnegrito'], valorEscolha2, cores['limpa']))
elif escolha == '3':
    print('O preço final será de {}R$ {:.2f}{}.'.format(cores['roxonegrito'], valorEscolha3, cores['limpa']))
elif escolha == '4':
    print('O preço final será de {}R$ {:.2f}{}.'.format(cores['verdenegrito'], valorEscolha4, cores['limpa']))
else:
    print('Opção incorreta. Tente novamente.')