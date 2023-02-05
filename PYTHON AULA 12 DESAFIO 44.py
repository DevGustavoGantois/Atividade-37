print('                                                       ATIVIDADE                                          ')
print('------------------------------------------------------------------------------------------------------------')
print('Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de')
print('pagamento:')

print('-à vista dinheiro/cheque: 10% de desconto.')

print('-à vista no cartão: 5% de desconto.')

print('-em até 2x no cartão: preço formal.')

print('-3x ou mais no cartão: 20% de juros.')
print('----------------------------------------------------------------------------------------------------------------')
print('{:=^40}'.format(' LOJAS GANTOIS '))
preco = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO:')
print('[1] À vista dinheiro/cheque.')
print('[2] À vista no cartão.')
print('[3] 2x no cartão.')
print('[4] 3x ou mais no cartão.')
opcao = int(input('Qual é a opção?'))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de {:.2f}R$'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparc= int(input('Quantas parcelas?'))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(totalparc, parcela))
else:
    total = 0
    print('OPÇÃO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE!')
print('Sua compra de {:.2f}R$ vai custar {:.2f}R$ no final'.format(preco, total))



