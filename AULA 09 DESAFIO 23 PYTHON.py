print('Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos serapados.')
print('Ex: Dígite um número: 1834')
print('Unidade: 4')
print('Dezena: 3')
print('Centena: 8')
print('Milhar: 1')
print('=====================================================================================================')
print('======================================================================================================')
numero = int(input('Digite um número:'))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(' Analisando o número : {}'.format(numero))
print('Sua Unidade é: {}'.format(u))
print('Sua dezena é: {}'.format(d))
print('Sua centena é: {}'.format(c))
print('Seu Milhar é: {}'.format(m))
print('=======================================================================================================')
print('===========================================================================================================')
print('DESAFIO 23 CONCLUIDO!')

