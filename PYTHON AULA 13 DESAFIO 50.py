print('                                               ATIVIDADE                ')
print('-----------------------------------------------------------------------------------')
print('Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o ')
print('valor for impar, desconsidere-o.')
print('--------------------------------------------------------------------------------------------------------------')
from time import sleep
soma = 0
cont = 0
print('PREPARANDO AS OPÇÕES...')
sleep(2)
for c in range(1, 7):
    num = int(input('Digite o {} valor:'.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números PARES e a soma foi {}.'.format(cont, soma))
print('FIM.')
