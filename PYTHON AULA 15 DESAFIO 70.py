print('                                       ATIVIDADE                                ')
print('-=-'*30)
print('Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai')
print('continuar ou não. No final, mostre:')

print('A) Qual é o gasto total na compra.')

print('B) Quantos produtos custam mais de R$1000.')

print('C) Qual é o nome do produto mais barato.')
print('---'*30)
print('>>>'*30)
print(' LOJA PREÇO DE BANANA ')
print('>>>'*30)
total = tot1000 = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto:'))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        tot1000 += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
        resp = ' '
        while resp not in 'SN':
            resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if resp == 'N':
            break
print('{:-^40}'.format('FIM DO PROGRAMA.'))
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {tot1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')