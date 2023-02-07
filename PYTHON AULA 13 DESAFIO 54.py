print('                                             ATIVIDADE                                       ')
print('====================================================================================================')
print('Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não')
print('antingiram a maior idade e quantas já são maiores.')
print('==========================================================================================================')
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}* pessoa nasceu?'.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
else:
    totmenor += 1
print('Ao todo tivemos {} pessoas maiores idade.'.format(totmaior))
print('Ao todo tivemos {} pessoas menores idade'.format(totmenor))
