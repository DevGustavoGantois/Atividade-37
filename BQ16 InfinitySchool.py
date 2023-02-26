print('                                ATIVIDADE               ')
print('------------------------------------------------------------------------------------------------------')
print('Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem decrescente.')
print('=='*40)
a = float(input('Valor 1° produto: '))
b = float(input('Valor 2° produto: '))
c = float(input('Valor 3° produto: '))
if a < c:
    a, c = c, a
elif a < b:
    a, b = b, a
elif b < c:
    b, c = c, b
print(f'A ordem decrescente é {a}, {b} e {c}')