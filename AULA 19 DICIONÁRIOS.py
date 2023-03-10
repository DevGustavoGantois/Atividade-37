print('DICIONÁRIOS.')
pessoas = {'nome': 'Gustavo', 'Sexo': 'Masculino', 'Idade': 19, 'Peso': 80}
print(f'O {pessoas["nome"]} tem {pessoas["Idade"]} anos')
pessoas['nome'] = 'Augusto'
for k, v in pessoas.items():
    print(f'{k}={v}')

brasil=[]
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 ={'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['sigla'])