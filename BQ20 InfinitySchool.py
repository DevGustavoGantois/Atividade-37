print('                                       ATIVIDADE                                       ')
print('------------------------------------------------------------------------------------------')
print('Faça um programa que receba a idade de dez pessoas, calcule e mostre a quantidade de pessoas com idade maior ou')
print('igual a 18 anos.')
print('=='*40)
quant = 0
for pessoas in range (1, 11):
    idades = int(input('Digite a idade de 10 indivíduos:'))
    if idades >= 18:
        quant += 1
print(f'Existem {quant} pessoas com a idade maior ou igual a 18 anos.')