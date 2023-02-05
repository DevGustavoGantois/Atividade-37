print('                                                      ATIVIDADE                                     ')
print('----------------------------------------------------------------------------------------------------------')
print('Crie um programa que faça o computador jogar Jokenpô com você!')
print('-----------------------------------------------------------------------------------------------------------')
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('Suas opções:')
print('[0] PEDRA.')
print('[1] PAPEL.')
print('[2] TESOURA.')
print('-=' * 11)
jogador = int(input('Qual a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(2)
print('PO!!!')
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA.!')
elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA.')
elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('JOGADOR VENCE!!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA.')

