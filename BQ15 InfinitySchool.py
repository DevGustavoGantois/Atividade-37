print('                               ATIVIDADE')
print('--------------------------------------------------------------------------------------')
print('Um posto está vendendo combustíveis com a seguinte tabela de descontos:')
print('-Alcool:')
print('          a) até 20 litros, desconto de 3% por litro.')
print('          b) acima de 20 litros, desconto de 5% por litro.')
print('-Gasolina:')
print('          a) até 20 litros, desconto de 4% por litro.')
print('          b) acima de 20 litros, desconto de 6% por litro.')
print('--------------------------------------------------------------------------------------')
print('Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificando da seguinte forma:)')
print('(A-álcool, G-gasolina). Calcule e imprima o valor a ser pago pelo cliente sabendo- se que o preço do litro de gasolina é')
print('R$ 2,50 o preço do litro do álcool é R$ 1,90.')
print('--'*40)
LA = float(input('Quantos L de Álcool?'))
LG = float(input('Quantos L de Gasolina?'))
if LA <= 20:
    A = 1.90 * LA
    A = LA * 3/100
    A = LA - A
    print(f'O número de litros de Alcool vendidos foi de {LA}. O valor a ser pago é de {A} R$ litros de alcool. ')
elif LA > 20:
    A20 = 1.90 * LA
    A20 = LA * 5/100
    A20 = LA - A20
    print(f'O número de litros de Alcool vendidos foi de {LA}. O valor a ser pago é de {A20} R$ litros de alcool.')
if LG <= 20:
    L = 2.50 * LG
    L = LG * 4/100
    L = LG - L
    print(f'O número de litros vendidos em Gasolina foi de {LG}. O valor a ser pago é de {L} R$ litros de Gasolina.')
elif LG > 20:
    L = 2.50 * LG
    L = LG * 6/100
    L = LG - L
    print(f'O número de litros vendidos em Gasolina foi de {LG}. O valor a ser pago é de {L} R$ litros de Gasolina.')
print('=='*40)
print('FIM DO PROGRAMA...')
