print('=====================================ATIVIDADE===================================================')
print("""Crie programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde
esses resultados em dicionário. No final, coloque esse dicionário em ordem, sabendo
em ordem, sabendo que o vencedor tirou o maior número no dado. """)
print('-='*40)
from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'Jogador1': randint(1, 6),
             'Jogador2': randint(1, 6),
             'Jogador3': randint(1, 6),
             'Jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados')
for k, v in jogadores.items():
    print(f'{k}, tirou o {v} no dado.')
    sleep(2)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse = True)
print('-='*40)
print('        ==RANKING DOS JOGADORES==')
for i, v in enumerate(ranking):
    print(f'{i+1} lugar {v[0]} com {v[1]}')
    sleep(2)
