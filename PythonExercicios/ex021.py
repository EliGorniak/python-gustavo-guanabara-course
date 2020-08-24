# Faça um programa em Python que abra e reproduza o àudio de um arquivo MP3.

# usando o pacote PyGame


import pygame

# Inicializando o mixer PyGame
pygame.mixer.init()

# Iniciando o Pygame
pygame.init()

pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()