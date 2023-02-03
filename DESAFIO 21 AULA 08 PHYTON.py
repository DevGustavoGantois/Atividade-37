print('Faça um programa em Phyton que abra e  reproduza o áudio de um arquivo MP3')
print('=============================================================================')
import pygame
pygame.init()
pygame.mixer.music.load('ex21.mp3')
pygame.mixer.music.play()
pygame.event.wait()