print('                                                      ATIVIDADE                                          ')
print('Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor')
print(' da casa, o salário do comprador e em quantos anos ele vai pagar.')
print('---------------------------------------------------------------------------------------------------------')
print('Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será')
print('apagado...')
print('---------------------------------------------------------------------------------------------------------------')
print('----------------------------------------------------------------------------------------------------------------')
casa = float(input('Qual o valor da casa R$:'))
comprador = float(input('Qual o salário do comprador R$:'))
anos = int(input('Quantos anos ele vai pagar?'))
prestaçao = casa / (anos * 12)
minimo = comprador * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos '.format(casa , anos) , end='')
print('A prestação será de R${:.2f}'.format(prestaçao))

print('COMPARANDO tem que pagar {} e o mínimo é de {}'.format(prestaçao , minimo))

if prestaçao <= minimo:
    print('EPRÉSTIMO PODE SER CONCEDIDO!')
else:
    print('EMPRÉSTIMO NEGADO!')

