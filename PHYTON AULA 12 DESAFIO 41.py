print('                                                   ATIVIDADE                     ')
print('----------------------------------------------------------------------------------------------')
print('A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua')
print('categoria, de acordo com a idade.')

print('- Até 9 anos: MIRIM')

print('Até 14 anos: INFANTIL')

print('-Até 19 anos: JÚNIOR')

print('-Até 25 anos: SÊNIOR')

print('-Acima de 25 anos: MASTER')
print('---------------------------------------------------------------------------------------------------------------')
print('                                           CONFEDERAÇÃO NACIONAL DE NATAÇÃO.                                   ')
nascimento = int(input('Qual o ano de nascimento desse atleta:'))
idade = (2023 - nascimento)
if idade == 9:
    print('O Atleta tem {}, nasceu em {} e será da categoria MIRIM até 9 anos.'.format(idade , nascimento))
elif idade <= 14:
    print('O Atleta tem {}, nasceu em {} e será da categoria INFANTIL até 14 anos.'.format(idade , nascimento))
elif idade <= 19:
    print('O Atleta tem {}, nasceu em {} e será da categoria JÚNIOR até 19 anos.'.format(idade , nascimento))
elif idade > 25:
    print('O Atleta tem {} anos, nasceu em {} e será da categoria MASTER acima de 25 anos.'.format(idade , nascimento))