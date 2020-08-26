# Manipulação de cadeia de caracteres - teoria

frase = 'Curso em Video Python'

# fatiamento de uma string
print(frase[9]) # mostra o caractere inserido na posição 9 da string
print(frase[9:14]) # mostra os caracteres inseridos nas posições 9 até 12 da string, o 14 ele exclui
print(frase[9:21]) # mostra os caracteres inseridos nas posições 9 até 20, já que 21 ele exclui
print(frase[9:21:2]) # mostra os caracteres inseridos nas posições 9 até 20, não mostra o 21 e pula de 2 em 2
print(frase[5:]) # mostra os caracteres começando da posição 5 até o final
print(frase[:5]) # mostra os caracteres começando da posição 0 até o 4
print(frase[15:]) # mostra o caractere inserido da posição 15 até o final
print(frase[9::3]) # mostra o caractere começando da posição 9 até o final:: mas vai pulando de 3 em 3

# análise de uma string
print(len(frase)) #qual o comprimento da frase, quantos caracteres
print(frase.count('o')) #contar quantas vezes a letra o minuscula aparecem
print(frase.upper().count('O')) # combinação de métodos, vai transformar todos os o em maiuscula e então contar quantos O tem na frase
print(frase.count('o', 0, 13)) #contar quantas vezes a letra o minuscula aparecem da posição 0 até 13, descontando o 13
print(frase.find('deo')) #procura o "deo" e diz em que posição ele inicia
print(frase.find('Android')) # procura essa string, se ela não existe, ele retorna o -1, que significa, falso
print('Curso' in frase) #procura essa string, se ela existir, retorna True

# Transformação de string
print(frase.replace('Python', 'Android')) #vai substituir a string Python por Android
print(frase.upper()) # transforma todos os caracteres da string pra maiuscula
print(frase.lower()) # transforma todos os caracteres da string pra miniscula
print(frase.capitalize()) #transforma somente o primeiro caractere pra maiuscula, todas as outras palavras vao permanecer em minuscula
print(frase.title()) #transforma o primeiro caractere de cada palavra em maiuscula

frase2 = '  Aprenda Python  '
print(len(frase2)) #qual o comprimento da frase, quantos caracteres
print(frase2.strip()) # remove todos os espaços em branco no começo e final da string
print(frase2.rstrip()) # remove apenas os espaços da direita/right, do final da string
print(frase2.lstrip()) # remove apenas os espaços da esquerda/left, do começo da string

# divisão na string
newsplit = frase.split()
print(frase.split()) #divide cada uma das palavras em novas strings criando uma nova lista, cada palavra agora começa pelo indice 0 - zero e faz parte da lista

# junção na string
print('-'.join(newsplit)) #coloca um hifen entre cada uma das palavras da lista anterior
print(newsplit[2][3]) #mostra o caractere na posição 3 da segunda palavra

# impressão de textos longos
print("""Bacon ipsum dolor amet pork loin biltong kevin bresaola tail. Burgdoggen turkey landjaeger tongue, ball tip chislic ham shank. Spare ribs cupim shank, pastrami beef ground round kielbasa leberkas strip steak. Pork chop prosciutto ground round ham, beef picanha burgdoggen tail filet mignon turducken. Prosciutto tenderloin corned beef kevin, andouille kielbasa ham hock jowl ham shankle meatball. Porchetta ham chuck pork chop hamburger. Kevin biltong brisket swine, ham hock jowl ham rump hamburger prosciutto pastrami capicola shank tri-tip.""")