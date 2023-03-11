from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome:'))
nasc = int(input('Ano de Nascimento:'))
dados['Idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem):'))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação:'))
    dados['Salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['Idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-='*40)
for k, v in dados.items():
    print(f'-{k} tem o valor {v}.')