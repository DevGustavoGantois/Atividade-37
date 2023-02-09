print('                                                           ATIVIDADE                            ')
print('======================================================================================================')
print('O computador vai pensar de um número entre 0 a 10. Só que agora o jogador vai tentar advinhar até acertar,')
print('mostrando no final quantos palpites foram necessários para vencer.')
print('------------------------------------------------------------------------------------------------------------')
from random import randint
computador = randint(0, 10)
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite?'))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez.')
        elif jogador > computador:
            print('Menos...Tente mais uma vez.')
print('Acertou com {} palpites. Parabéns!'.format(palpites))

