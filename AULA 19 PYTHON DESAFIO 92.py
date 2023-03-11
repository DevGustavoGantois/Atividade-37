print('==========================================ATIVIDADE===============================================')
print("""Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o
(com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá
também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos
a pessoa vai se aposentar. """)
print('-='*40)
from datetime import datetime
dados = dict()
dados['Nome']= str(input('Nome:'))
nasc = int(input('Data de nascimento:'))
dados['Carteira de Trabalho'] = int(input('Carteira de Trabalho (0 não tem):'))
dados['Ano de contratação'] = int(input('Ano de Contratação:'))
dados['Salário'] = float(input('Salário: R$'))
dados['Idade'] = datetime.now().year - nasc
dados['Aposentadoria'] = dados['Idade'] + ((dados['Ano de contratação'] + 35) - datetime.now().year)
print('-='*40)
if dados['Carteira de Trabalho'] > 0:
    print(f'O nome é {dados["Nome"]}.')
    print(f'Idade é = {dados["Idade"]}')
    print(f'CPTS tem o valor de: {dados["Carteira de Trabalho"]}')
    print(f'Salário tem o valor de: {dados["Salário"]}')
    print(f'A aposentadoria de {dados["Nome"]} será em {dados["Aposentadoria"]}')
if dados['Carteira de Trabalho'] == 0:
    print(f'O nome é {dados["Nome"]}.')
    print(f'A idade é = {dados["Idade"]}.')
    print(f'CTPS tem o valor de {dados["Carteira de Trabalho"]}')
print('=-'*40)
print('FIM DO PROGRAMA...')
