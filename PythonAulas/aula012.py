# Condicionais aninhadas

nome = str(input('Qual é seu nome? '))
# ===== estrutura condicional aninhada ======
if nome == 'Gustavo':
    print('Que nome bonito"')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Pedro':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino.')
else:
    print('Seu nome é muito bonito!')
# =============================================

print('Tenha um bom dia, {}!'.format(nome))