print('                                                            ATIVIDADE                             ')
print('-----------------------------------------------------------------------------------------------------')
print('Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:')
print('5!= 5 x 4 x 3 x 2 x 1 = 120')
print('===============================================================================================')
from math import factorial
print('-=-'*10)
numero = int(input('Digite um número para calcular o seu fatorial:'.format(factorial)))
print('Calculando {}!'.format(numero))
f = factorial(numero)
print('O fatorial de {} é {}'.format(numero, f))