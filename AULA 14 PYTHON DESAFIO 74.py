print('============================================ATIVIDADE==========================================')
print('Crie um programa que vai gerar 5 números aleatórios e colocar em uma Tupla. Depois disso, mostre a listagem')
print('de números gerados e também indique o menor e o maior valor que estão na Tupla.')
print('=='*40)
from random import randint
sorteado = (randint(1, 10) , randint(1, 10) , randint(1, 10) , randint(1, 10) , randint(1, 10))
print('Os valores sorteados foram:', end= '')
for n in sorteado:
    print(f'{n}', end='' )
print(f'\nO maior valor sorteado foi {max(sorteado)}.')
print(f'O menor valor sorteado foi{min(sorteado)}.')