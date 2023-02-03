print('                                  ATIVIDADE                               ')
print('--------------------------------------------------------------------------------------')
print('Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele vai se alistar')
print('ou se já passou do tempo de alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.')
print('---------------------------------------------------------------------------------------------------------------------')
print(' ==================================ALISTAMENTO==========================================')
print('-----------------------------------------------------------------------------------------')
print('CASO TENHA 18 ANOS EU TERÁ QUE SE ALISTAR...')
ano = int(input('Qual sua data de nascimento:'))
Didade = (2023 - ano)
if Didade >= 18:
    print('O índividuo terá que se alistar pois tem mais de 18 anos. Ele terá {} anos.'.format(Didade))
elif Didade < 18:
    print('O individuo terá menos de 18 anos e não terá que se alistar no exercíto. Ele terá {} anos.'.format(Didade))
print('Ele nasceu em {}'.format(Didade))


