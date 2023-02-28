print('                                           ATIVIDADE                                       ')
print('=='*40)
print('Faça um programa que receba o valor de um carro e mostre uma tabela com os seguintes dados: preço final, quantidade')
print('de parcelas e valor de cada parcela.')
print('=='*40)
print('Considere o seguinte:')
print('- O preço final para compra à vista tem um desconto de 20%;')
print('-As quantidades de parcelas podem ser: 6, 12, 18, 24, 30, 36, 42, 48, 54, 60.')
print('- Os percentuais de acréscimo seguem a tabela a seguir:')
print('>>06 - 03%')
print('>>12 - 06%')
print('>>18 - 09%')
print('>>24 - 12%')
print('>>30 - 15%')
print('>>36 - 18%')
print('>>42 - 21%')
print('>>48 - 24%')
print('>>54 - 27%')
print('>>60 - 30%')
print('=='*40)
#valor do carro = vamos usar a variável valor.
#mostrar preço final.
#mostrar a quantidade de parcela. 
#valor de cada parcela.
#preço final= usar uma váriavel FINAL tem que ser a vista com desconto de 20%.
#percentual de acrescimo.
valor = float(input('Digite o valor do carro:'))
desconto = valor * 0.20
print(f'Compras à vista tem desconto 20% de {valor}R$ por {valor - desconto}R$! \n')
print('Os percentuais de acréscimo seguem a tabela a seguir:\n 6 = 03% \n 12 = 06% \n 18 = 09% \n 24 = 12% \n 30 = 15% \n 36 = 18% \n 42 = 21% \n 48 = 24% \n 54 = 27% \n 60 = 30%"')

parcela6 = valor * 0.03
parcela12 = valor * 0.06
parcela18 = valor * 0.09
parcela24 = valor * 0.12
parcela30 = valor * 0.15
parcela36 = valor * 0.18
parcela42 = valor * 0.21
parcela48 = valor * 0.24
parcela54 = valor * 0.37
parcela60 = valor * 0.30

print(f"o valor total {parcela6+valor} com parcelas de {(parcela6+valor)/6}\n")
print(f"o valor total {parcela12+valor} com parcelas de {(parcela12+valor)/12}\n")
print(f"o valor total {parcela18+valor} com parcelas de {(parcela18+valor)/18}\n")
print(f"o valor total {parcela24+valor} com parcelas de {(parcela24+valor)/24}\n")
print(f"o valor total {parcela30+valor} com parcelas de {(parcela30+valor)/30}\n")
print(f"o valor total {parcela36+valor} com parcelas de {(parcela36+valor)/36}\n")
print(f"o valor total {parcela42+valor} com parcelas de {(parcela42+valor)/42}\n")
print(f"o valor total {parcela42+valor} com parcelas de {(parcela42+valor)/42}\n")
print(f"o valor total {parcela48+valor} com parcelas de {(parcela48+valor)/48}\n")
print(f"o valor total {parcela54+valor} com parcelas de {(parcela54+valor)/54}\n")
print(f"o valor total {parcela60+valor} com parcelas de {(parcela60+valor)/60}\n")