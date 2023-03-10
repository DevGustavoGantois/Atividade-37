print('====================================ATIVIDADE==============================================================')
print("""Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar
quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando
tudo em uma lista composta.""")
print('-='*40)
from random import randint
from time import sleep
palpite = [[], [], [], [], [], []]
numero = int(input('Quantos jogos você quer que eu sorteie?'))
palpite.append(numero)

