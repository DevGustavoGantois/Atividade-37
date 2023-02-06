print('                                          ATIVIDADE                                                   ')
print('-----------------------------------------------------------------------------------------------------------')
print('Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no')
print('intervalo de 1 até 500.')
print('--------------------------------------------------------------------------------------------------------------')
input('Aperte Ok para saber a soma entre todos os números múltiplos de três até 500:')
print('ANALISANDO OS NÚMEROS...')
cont = 0
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))

