from random import randint
computador = randint(0,5) # FAZ O COMPUTADOR '' PENSAR ''
print('-=-' * 10)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei?')) # Jogador tenta advinhar
if jogador == computador:
    print('Parabéns!! você conseguiu me vencer!')
else:
    print('Ganhei!! eu pensei no número {} e não no número {}!'.format(computador, jogador))


