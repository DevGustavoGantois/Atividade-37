print('                                               ATIVIDADE                                                   ')
print('--------------------------------------------------------------------------------------------------------------')
print('Programa que lê o primeiro termo e a razão de uma PA. No final, mostra os 10 primeiros termos de')
print('progressão.')
print('---------------------------------------------------------------------------------------------------------------')
print('-=' * 40)
print('10 TERMOS DE UMA PA')
print('-=' * 40)
primeiro = 0
razao = 0
decimo = primeiro + (10-1) * razao
primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
for x in range(primeiro, decimo, razao):
    print('{}'.format(x), end='->')
print('ACABOU.')
