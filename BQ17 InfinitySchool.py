print('                                        ATIVIDADE                           ')
print('=='*40)
print('Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço normal de etiqueta')
print('(peça pra que o usuário) e a escolha da condição de pagamento. Utilize os códigos feitos da tabela a seguir para')
print('=='*40)
print('ler qual a condição de pagamento escolhida e efetuar o cálculo adequeado.')
print('[1]- À vista em dinheiro ou cheque, recebe 15 porcento de desconto.')
print('[2]- À vista no cartão de crédito, recebe de 10 porcento de desconto.')
print('[3]- Em duas vezes, preço normal de etiqueta sem juros.')
print('[4]- Em duas vezes, preço normal de etiqueta com mais juros de 10porcento.')
print('=='*40)
produto_preçonormal = float(input('Digite o valor do produto:'))
print('FORMAS DE PAGAMENTO:')
forma1 = print('[1]- À vista em dinheiro ou cheque, recebe 15 porcento de desconto.')
forma2 = print('[2]- À vista ou no cartão de credito, recebe 10porcento de desconto.')
forma3 = print('[3]- Em duas vezes, preço normal de etiqueta sem juros.')
forma4 = print('[4]- Em duas vezes, preço normal de etiqueta com mais juros de 10%')
print('=='*40)
forma_pagamento = str(input('Qual a condição escolhida do pagamento:'))
if forma_pagamento == '1':
    forma_pagamento = forma1
    forma1 = produto_preçonormal * 15/100
    forma1 = produto_preçonormal - forma1
    print(f' A forma de pagamento do valor de {produto_preçonormal} à vista em dinheiro ou cheque, recebe 15 porcento de desconto e o valor é = {forma1:.2f}.  ')
elif forma_pagamento == '2':
    forma_pagamento = forma2
    forma2 = produto_preçonormal * 10/100
    forma2 = produto_preçonormal - forma2
    print(f'A forma de pagamento do valor de {produto_preçonormal} à vista ou no cartão de credito com 10% de desconto é = {forma2:.2f}R$. ')
elif forma_pagamento == '3':
    forma_pagamento = forma3
    forma3 = produto_preçonormal + (1) * 2
    print(f'O valor é {produto_preçonormal} e em duas vezes, preço normal de etiqueta sem juros é = {forma3:.2f}R$.')
elif forma_pagamento == '4':
    forma_pagamento = forma4
    forma4 = produto_preçonormal + (1 + 0.10) * 2
    print(f'O valor é {produto_preçonormal} e em duas vezes, preço normal de etiqueta com mais juros de 10% é = {forma4:.2f}R$.')
print('=='*40)
print('FIM DO PROGRAMA...')


