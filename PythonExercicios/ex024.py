# Crie um programa que leia o nome de uma cidade e diga se ela COMEÇA com o nome "SANTO"

cidade = str(input("Digite o nome da cidade em que você nasceu: ")).strip()
#strip() vai cortar todos os espaços entre as palavras e evitar que o contador inicie a contagem dos caracteres nos espaços

print(cidade[:5].upper() == 'SANTO')
# lê do primeiro ao quinto caractere e transforma todas em maiusculas, evitando que ele dê um FALSE por conta de maiuscula e minuscula
