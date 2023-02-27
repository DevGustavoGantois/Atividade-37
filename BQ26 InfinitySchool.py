print('                                                      ATIVIDADE                         ')
print('=='*60)
print('Uma loja A de carros deseja cadastrar 5 compras e verificar se o faturamento dessa loja A foi superior a')
print('loja B (faturamento = 54000). Se o faturamento atingir esse valor mostre na tela uma mensagem contendo em')
print('quanto foi superado o faturamento. Se não mostre quanto faltou para atingir o faturamento.')
#loja B Fatura 54 mil
#loja A de carros deseja cadastrar 5 compras.
#Se passar de 54mil mostre o quanto foi superado o faturamento da LojaA pela LojaB.
#Se não passar de 54mil mostre o quanto faltou para atingir o faturamento.
print('                                          LOJA DE CARROS                               ')
print('=='*60)
lojab = 54000
lojaa = float(input('Qual foi o faturamento da Loja A:'))
print('O faturamento da Loja B é 54000')
if lojaa > lojab:
    maior = lojaa - lojab
    print('O faturamento da Loja A foi de {} e superou o faturamento da Loja B em {}. '.format(lojaa, maior ))
else:
    menor = lojab-lojaa
    print(f'Faltou {menor} para o faturamento de Loja A: {lojaa} atingir o faturamento de Loja B: {lojab}.')
print('=='*40)
print('FIM DO PROGRAMA...')