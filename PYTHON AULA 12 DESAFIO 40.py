print('                                          ATIVIDADE                        ')
print('-------------------------------------------------------------------------------------------')
print('Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo ')
print('com a média atingida:')

print('-Média abaixo de 5.0: REPROVADO')

print('-Média entre 5.0 e 6.9: RECUPERAÇÃO ')

print('-Média entre 7.0 ou superior: APROVADO')
print('----------------------------------------------------------------------------------------------------------------')
print('                                  BOLETIM.                                                         ')
print('                              MÉDIA ESCOLAR                                                       ')
aluno1 = float(input('Qual a nota do primeiro aluno:'))
aluno2 = float(input('Qual a nota do segundo aluno:'))
media = (aluno1 + aluno2) /2
if media < 5.0:
    print('Você tirou {} tirou uma nota abaixo de 5.0 e terá que ser REPROVADO.'.format(media))
elif media <= 6.9:
    print('Você tirou {} e está de RECUPERAÇÃO...'.format(media))
elif media >= 7.0:
    print('Parabéns, você tirou {} e passará de ano!'.format(media))