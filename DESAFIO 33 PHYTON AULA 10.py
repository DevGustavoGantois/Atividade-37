print('                           ATIVIDADE                             ')
print('==================================================================')
print('Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.')
print('===============================================================================')
p = int(input('Digite o primeiro número:'))
s = int(input('Digite o segundo número:'))
t = int(input('Digite o terceiro número:'))
# Verificando quem é menor...
menor = p
if s < p and p < t:
    menor = s
if t < p and t < s:
    menor = t
# Verificando quem é maior...
maior = p
if s > p and s > t:
    maior = s
if t > p and t > s:
    maior = t
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))