#Você possui dados de vendas trimestrais de uma empresa em uma lista. Cada trimestre é representado
#como uma lista de números, onde cada número representa o valor de vendas de um mês (janeiro a
#março, abril a junho, julho a setembro e outubro a dezembro).
#Você deve realizar as seguintes tarefas: Calcule a média de vendas por trimestre.

total_salles = []

months_salles = {
    'March': 93,
    'April': 60,
    'June': 110,
    'July': 324,
    'September':200,
    'October':333,
    'December':444
}

organize_salles = {
    'Q1': months_salles['March'] + months_salles['April'] + months_salles['June'] / 3, 
    'Q2': months_salles['July'] + months_salles['September'] + months_salles['October'] / 3,
    'Q3': months_salles['December']
}

average_salles = sum(months_salles.values()) / len(organize_salles)

print(f"The months with prices is -> {months_salles}")
print(f"The average salles is -> {average_salles}")