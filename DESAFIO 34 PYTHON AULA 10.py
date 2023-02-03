print('                                            ATIVIDADE                                           ')
print('=================================================================================================')
print('Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.')

print('Para salários superiores a R$ 1250.00 , calcule um aumento de 10%')
print('Para inferiores ou iguais, o aumento é de 15%.')
print('==================================================================================================')
salario = float(input('Qual o salário do funcionário R$??'))
if salario <= 1250:
    novo = salario + (salario * 15/100)
else:
    novo = salario + (salario * 10/100)
print('Quem ganhava R$ {:.2f} passa a ganhar {:.2f} agora'.format(salario , novo))