print('===========================================ATIVIDADE=========================================================')
print('Crie um programa que tenha uma Tupla única com nomes de produtos e seus respectivos preços, na sequencia.')
print('No final, mostre uma listagem de preços, organizando os dados em forma tabular.')
print('=='*40)
print('                             LISTAGEM DE PREÇOS                                ')
print('=='*40)
produtos = ('Mouse', 10.50 , 'Caneta', 5.99 , 'Caderno', 55.99 , 'Celular', 3000.99 , 'Calça', 100.50 , 'Camisa', 29.99 , 'Bermuda', 45.75, 'Agenda', 32.99 , 'Mochila', 300.00 , 'Relógio', 1500.00)
print('--'*40)
print(f'{"LISTAGEM DE PREÇOS:^40"}')
print('--'*40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')
print('--'*40)
