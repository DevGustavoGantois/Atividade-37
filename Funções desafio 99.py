print('=================================ATIVIDADE===========================================================')
print("""Faça um programa que tenha uma função chamada maior(), que receba vários parãmetros com
valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior. """)
print('-='*40)
from time import sleep

def maior(*v):
    cont = maior = 0
    print('-'*40)
    print('\nAnalisando os valores passados...')
    for n in v:
        print(f'{v}', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        cont += 1
        print(f'Foram informados {cont} valores ao todo.')
        print(f'O maior valor informado foi {maior}')
    




#Programa pricipal
print('-='*40)
maior(1, 3, 4, 5, 6, 9, 12, 15)
maior(3, 5, 15)
maior(1, 3)
maior()


