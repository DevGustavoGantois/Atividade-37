#Analise de Produção anual
#Você tem um conjunto de dados que contém informações sobre a produção anual de diferentes culturas em diversas
#fazendas ao longo de vários anos. O objetivo é realizar uma análise simples desses dados usando apenas as
#funções agregadoras. Tarefas: Encontre o ano em que a produção total foi máxima e o ano em que foi mínima.

#Identifique a cultura que teve a maior produção total e a cultura com a menor produção total ao longo dos anos.
#Encontre a fazenda que obteve a produção máxima em um determinado ano e a fazenda com a produção mínima no
#mesmo ano. - Construa seus próprios dados fictícios.

production_data = {
    2010:{'Wheat': 10.000, 'Sugar': 80.000, 'Corn': 35.000},
    2011:{'Wheat': 20.000, 'Sugar': 100.000, 'Corn': 55.000},
    2012:{'Wheat': 30.000, 'Sugar': 150.000, 'Corn': 75.000},
    2013:{'Wheat': 50.000, 'Sugar': 200.000, 'Corn': 95.000},
    2014:{'Wheat': 70.000, 'Sugar': 400.000, 'Corn': 120.000},
    2015:{'Wheat': 100.000, 'Sugar': 500.000, 'Corn': 140.000},
    2016:{'Wheat': 150.000, 'Sugar': 600.000, 'Corn': 170.000},
    2017:{'Wheat': 250.000, 'Sugar': 700.000, 'Corn': 200.000},
    2018:{'Wheat': 300.000, 'Sugar': 800.000, 'Corn': 400.000},
    2019:{'Wheat': 400.000, 'Sugar': 900.000, 'Corn': 500.000},
    2020:{'Wheat': 550.000, 'Sugar': 920.000, 'Corn': 550.000},
    2021:{'Wheat': 550.000, 'Sugar': 950.000, 'Corn': 800.000},
    2022:{'Wheat': 800.000, 'Sugar': 980.000, 'Corn': 950.000},
    2023:{'Wheat': 900.000, 'Sugar': 1000.000, 'Corn': 999.999} 
}

#Econtrar a produção máxima e produção mínima dos produtos acima no dicionário:

max_product_year = max(production_data, key=lambda year: sum(production_data[year].values()))
min_product_year = min(production_data, key=lambda year: sum(production_data[year].values()))

print("The Year of max production data is ->", max_product_year)
print("The Year of min production data is ->", min_product_year)

#Encontrando o valor da fazenda com o maior e o menor valor de produção durante os anos:
max_culture = max(production_data[max_product_year], key=production_data[max_product_year].get)
min_culture = min(production_data[min_product_year], key=production_data[min_product_year].get)

print("The max culture in years is ->", max_culture)
print("The min culture in years is ->", min_culture)

#Encontrar a fazenda que produziu a quantidade máxima e mínima no mesmo ano

max_culture_farm_year = max(production_data[max_product_year], key=production_data[max_product_year].get)
min_culture_farm_year = min(production_data[min_product_year], key=production_data[min_product_year].get)

print("The max culture farm in year is ->", max_culture_farm_year)
print("The min culture farm in year is ->", min_culture_farm_year)