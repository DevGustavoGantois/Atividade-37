print('                                            ATIVIDADE                           ')
print('-----------------------------------------------------------------------------------------')
print('Faça um programa que receba a idade e o peso de sete pessoas. Calcule e mostre:')
print('-A quantidade de pessoas com mais de 90kg.')
print('-A média das idades das sete pessoas.')
print('=='*40)
mais90 = 0
media = 0
for pessoa in range (1, 8):
 idade = int(input('Qual a idade do indivíduo:'))
 peso = float(input('Qual o peso do indivíduo (kg):'))
 media = media + idade
 if peso > 90:
   mais90 += 1
print(f'Existem {mais90} com mais de 90kg. ')
print(f'Á média de idade é de {media / 7}.')
