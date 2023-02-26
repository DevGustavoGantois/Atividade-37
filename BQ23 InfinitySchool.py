print('                                      ATIVIDADE                             ')
print('--------------------------------------------------------------------------------')
print('Faça um programa que verifique e mostre  os números entre 1.000 e 2.000 (incluso) que, quando dividos por 11,')
print('produzam o resto igual a 2.')
print('=='*40)
for numero in range(1000, 2000):
    if numero % 11 == 2:
        print(f'{numero:.2f}')
print('=='*40)
print('FIM DO PROGRAMA.')
