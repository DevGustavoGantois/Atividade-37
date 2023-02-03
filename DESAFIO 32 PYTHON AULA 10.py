print('                                                 ATIVIDADE                   ')
print('=====================================================================================')
print('Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.')
print('-------------------------------------------------------------------------------------')
from datetime import date
ano = int(input('Digite um ano:...Coloque 0 para analisar o ano atual:'))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    ano = date.today().year
    print('Esse ano {} é ano bissexto'.format(ano))
else:
    print('Esse ano {} não é um ano bissexto.'.format(ano))


