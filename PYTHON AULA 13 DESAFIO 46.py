print('                                              Atividade                                           ')
print('------------------------------------------------------------------------------------------------------')
print('Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 0 a 10,')
print('com a pausa de 1 segundo entre eles.')
print('----------------------------------------------------------------------------------------------------------------')
from time import sleep
print('VAI COMEÇAR A CONTAGEM REGRESSIVA PARA OS FOGOS!!')
str(input('Digite OK para começar a contagem:'))
for c in range(0, 11):
    print(c)
    sleep(1)
print(' UHUUUUUU...Quantos fogos!!')
print('FIM!')


