#Encontre o trimestre com a maior soma de vendas.
#Encontre o trimestre com a menor soma de vendas.
#Calcule o total de vendas no ano inteiro.
#- Construa seus dados fictícios

#utilizei um dicionário para adicionar todos os meses do ano:
months_salles = {
    'January':124,
    'February':333,
    'March': 564,
    'April': 111,
    'May': 1000,
    'June': 222,
    'July': 123,
    'August': 55,
    'September': 12,
    'October': 453,
    'November': 666,
    'December': 777
}

#Fiz um dicionário somando os meses da empresa por trimestre: 
quarter_salles = {
    'Q1': months_salles['January'] + months_salles['February'] + months_salles['March'],
    'Q2': months_salles['April'] + months_salles['May'] + months_salles['June'],
    'Q3':months_salles['July'] + months_salles['August'] + months_salles['September'],
    'Q4':months_salles['October'] + months_salles['November'] + months_salles['December']
}

#Criando uma variável max_quarter para obter o máximo dos preços através da função agredadora max, dentro dessa função peguei o valor da chave(key) e extrai o maior valor.
max_quarter = max(quarter_salles, key=quarter_salles.get)
#Criando uma variável min_quarter para obter o mínimo dos preços através da função agregadora min, dentro dessa função peguei o valor da chave(key) e extrai o menor valor.
min_quarter = min(quarter_salles, key= quarter_salles.get)
#Criei a variável média total de vendas para somar todos os valores dentro do dicionário months_salles.
total_average_salles = sum(months_salles.values())

#Exibi a maior média de valores:
print(f'Total Average max: {max_quarter}')
#Exibi a menor média de valores: 
print(f'Total Average min: {min_quarter}')
#Exibi a média da soma dos valores de todos os meses da empresa:
print(f"The total average salles: {total_average_salles}")