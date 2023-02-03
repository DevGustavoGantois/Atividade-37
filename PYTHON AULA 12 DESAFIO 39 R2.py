print(' PROGRAMA DE ALISTAMENTO.')
from datetime import date
atual = date.today().year
nascimento = int(input('Qual o seu ano de nascimento?'))
idade = atual - nascimento
print('Quem nasceu em {} ano tem {} em {}'.format(nascimento, idade , atual))
if idade == 18:
    print('Você tem 18 anos e tem que se alistar IMEDIATAMENTE...')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento.')
    ano = atual + saldo
    print('Seu alistamento será em {} ano'.format(ano))
elif idade > 18:
    saldo = 18 - idade
    print('Você já tem 18 anos e deveria ter se alistado há {} anos...')
    ano = atual - saldo
    print(' Seu alistamento será em {} ano '.format(ano))
