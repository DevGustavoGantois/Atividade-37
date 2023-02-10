print('                                                        ATIVIDADE                                        ')
print('------------------------------------------------------------------------------------------------------------')
print('Leia o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while')
print('Gerador de PA:')
print('-=-'*40)
primeiro = int(input('Qual o primeiro termo:'))
razao = int(input('Qual é a razão da PA:'))
termo = primeiro
cont = 1
PA = termo + (10-1) * razao
print('-=-'*40)
while cont <= 10:
    print('{} ->'.format(termo), end='')
    termo+= razao
    cont += 1
print('FIM.')
