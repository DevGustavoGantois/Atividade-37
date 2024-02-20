#1)Dada uma lista de números, crie uma nova lista contendo
#apenas os números pares.


#OBS-> COMENTEI TODOS OS CÓDIGOS PARA FIXAÇÃO DO MEU APRENDIZADO, MAS O QUE EU FIZ NÃO É UMA PRÁTICA DO CLEAN CODE..



#Criei uma lista com vários números:
list_numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,16,17,18,19,20,21,22,23,24]

print('The pair numbers in list:')
#Utilizei o for para percorrer a lista de números 
for pair in list_numbers:
    #Caso o número fosse dividido por 2 e fosse igual a zero ele iria imprimir esses números da lista:
    if pair % 2 == 0:
        print(pair)      

#2)Crie um dicionário com informações de produtos, incluindo nome, preço e quantidade em estoque.
#Implemente funções para adicionar, remover e atualizar produtos no dicionário.


#Criei um dicionário contendo todas as informações dos produtos:
information_products = []

#Função principal dessa questão, contendo as opções e junto a elas as funções reutilizaveis com cada função 
def main():
    while True:
        print("PRODUCTS LIST")
        print("<=============================>")
        print("1- Add Product.")
        print("2- Remove Product.")
        print("3- Update product.")
        print("4- Exit the program.")
        print("<============================>")

        #Criei uma variável option para o usuário poder escolher de acordo com o Menu acima:
        option = int(input("Enter a option:"))

        #Se o usuário escolher o número 1,2,3,4 ele vai chamar as respectivas funções que criei separadamente
        if option == 1:
            add_product()
        elif option == 2:
            remove_product()
        elif option == 3:
            update_product()
        elif option == 4:
            print("Finished the program...")
            break
        #Caso digite um número fora do range de 1-4 ele falara que o valor não existe e pedirá para inseri-lo novamente
        else:
            print("The value is not exist. Please try again...")

#Esta função adiciona o nome, preço, quantidade e coloca todas as informações dentro de um dicionário:
def add_product():
     name = input("Enter a name of product:")
     price = float(input("Enter a price of product:"))
     quantity = int(input("What is the quantity of product:"))
     add_information_products = {'name': name, 'price': price, 'quantity': quantity}
     #Adicionando o dicionário add_information_products dentro da lista que criei
     information_products.append(add_information_products)

#Esta função remove o produto
def remove_product():
    #Pergunta ao usuário qual o produto que ele deseja remover:
    name = input("You want to remove some product:")
    #percorre a lista information_products
    for product in information_products:
        #Se o produto for igual o nome
        if product['name'] == name:
        #O programa irá remover o nome do produto dentro da lista através da função remove.
            information_products.remove(name)

#Esta função é de atualizar o produto, preço, quantidade...
def update_product():
    #Pergunta ao usuário qual o produto ele deseja atualizar:
    name = input("You want to update some product:")
    #Percorre a lista information_products
    for product in information_products:
        #Se o produto for igual o nome que o usuário colocar
        if product['name'] == name:
            #Ele pedirá novamente o preço e a quantidade dos produtos para atualiza-los
            price = float(input("Enter a updated price of product:"))
            quantity = int(input("Enter a updated quantity of product:"))
            #Adicionando o novo preço:
            product['price'] = price
            #Adicionando a nova quantidade:
            product['quantity'] = quantity
            print(f"{name} update is sucessfuly")
            break
        print(f"{name} not found in the products list.")
                        

#Utilizando o if __name__ == '__main__' para mostrar que o programa princípal que deverá rodar é o def main().
if __name__ == '__main__':
    main() 

#3)Crie um conjunto com nomes de cores. Implemente um função que retorne as cores 
#que têm mais de quatro letras.


#Criei um dicionário set_collors, nele contem várias cores.
set_colors = {'Blue', 'Red', 'Green', 'Yellow', 'Purple', 'Pink', 'Black', 'Magenta'}

#Criei uma função colors para retornar as cores que tenham mais de 4 letras.
def colors():
    #Lógica da questão: para que o color dentro do dicinário set_colors seja retornado, se ele tiver mais que 4 letra ele será mostrado
    #Utilizei a função len para percorrer as letras das cores dentro do dicionário.
    return {color for color in set_colors if len(color) > 4}

result_colors_more_than_four_letters = colors()
print("The Color more than four letters ->", result_colors_more_than_four_letters)


#4)Crie uma função que receba uma lista de strings e retorne uma nova lista contendo apenas as strings palíndromos.

#Criei uma função strings palidromes que recebe um argumento string_list
def palindrome_strings(string_list):
    #Criei uma variável palidromes que verifica enquanto o s de string in string list(argumento) se a string for igual a string invertida ela retornará as palavras palindromes:  
    palindromes=[s for s in string_list if s.lower() == s.lower()[::-1]]
    return palindromes

#Lista com as palavras
palindrome_list = ['arara', 'Gustavo', 'Duda', 'Nova', 'Nayra', 'Frida']

#Criando uma variável e dentro dessa variável está a função junto com a lista 
result_palidrome_strings = palindrome_strings(palindrome_list)
#Exibindo a resposta:
print("The palindrome strings is ->", result_palidrome_strings)

#5)Dado um dicionário que representa as vendas de produtos, encontre o produto mais vendido (ou os
#produtos mais vendidos, se houver um empate).

#Criando um dicionário com todos os produtos da loja.
salles_products = {
    'Bed': 10.000,
    'Table': 4.000,
    'Keyboard':15.000,
    'TV': 20.000,
    'Computer': 30.000
}

#Utilizando uma variável para adicionar o valor máximo do dicionário 
max_salles_product = max(salles_products.values())
#Depois percorro o dicionário com o product para exibir produto e a quantidade dentro do dicionário
for product, quantity in salles_products.items():
#Se o valor máximo daquele produto for igual a sua quantidade 
    if max_salles_product == quantity:
        #Eu irei imprimir a o produto e a quantidade do mesmo:
        print(f"The product with more salle {product}:{quantity}")
    

#6)Receba uma lista de números e use funções agregadoras para contar quantos valores são ímpares e quantos são pares.

numbers = [1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20]


#print("Pair numbers:")
#6)Receba uma lista de números e use funções agregadoras para contar quantos valores são ímpares e quantos são pares.

numbers = [0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20]
#1.PRIMEIRO JEITO

pair_numbers = [number for number in numbers if number % 2 == 0]
odd_number = [number for number in numbers if number % 2 == 1]

print("Pair numbers:",pair_numbers)
print("Odd numbers:", odd_number)

print(f"Exist {len(pair_numbers)} pair numbers in list.")
print(f"Exist {len(odd_number)} odd numbers in list.")


#2.JEITO DE RESOLVER ESSA QUESTÃO:
#print("Pair numbers:")
#for number_pair in numbers:
    #if number_pair % 2 == 0:
        #print(number_pair)
#print("Odd numbers:")
#for number_odd in numbers:
    #if number_odd % 2 == 1:
        #print(number_odd)

#print(f"Exist -> {len(number_pair)} pair numbers.")
#print(f"Exist -> {len(number_odd)} odd numbers.")


#7)Você possui dados de vendas trimestrais de uma
#empresa em uma lista. Cada trimestre é representado como uma lista de números, onde cada número
#representa o valor de vendas de um mês (janeiro a março, abril a junho, julho a setembro e outubro a
#dezembro).Você deve realizar as seguintes tarefas: Calcule a média de vendas por trimestre.


#Criei um dicionário com os meses e as vendas.
month_salles = {
    'January': 50.000,
    'March': 20.000,
    'April': 40.000,
    'June': 70.000,
    'July':90.000,
    'September': 120.000,
    'October': 200.000,
    'December': 500.000
}

#Criei uma variável com os trimestres e peguei a chave de cada trimestre e somei elas:
quarter_salles = {'Q1': [month_salles['January'] + month_salles['March'] + month_salles['April']],
                'Q2': [month_salles['June'] + month_salles['July']+ month_salles['September']],
                'Q3': [month_salles['October'] + month_salles['December']]}

#3 variáveis que vão receber a média de vendas do mês 1,2,3
#Utilizei a função agregadora sum para somar todos os valores do 1 trimestre e a função len para percorrer todos esses valores
average_quarter_salles1 = sum(quarter_salles['Q1']) / len(quarter_salles['Q1'])
#Utilizei da mesma lógica para as demais variáveis.
average_quarter_salles2 = sum(quarter_salles['Q2']) / len(quarter_salles['Q2'])
average_quarter_salles3 = sum(quarter_salles['Q3'])/ len(quarter_salles['Q3'])

# Mostrando as médias dos trimestres com o print
print(f"Average in 1 quarter:{average_quarter_salles1}")
print(f"Average in 2 quarter:{average_quarter_salles2}")
print(f"Average in 3 quarter:{average_quarter_salles3}")

#Mostrando a média geral de vendas do ano.
geral_average_salles = sum(month_salles.values())/ len(month_salles)
#Exibindo-as:
print(f"The geral average of salles is ->", geral_average_salles)


#8)Encontre o trimestre com a maior soma de vendas. Encontre o trimestre com a 
#menor soma de vendas. Calcule o total de vendas no ano inteiro.
#- Construa seus dados fictícios

month_of_salles = {
    'January': 50.000,
    'February': 100.000,
    'March': 20.000,
    'April': 40.000,
    'May': 600.000,
    'June': 70.000,
    'July':90.000,
    'August': 10.000,
    'September': 120.000,
    'October': 200.000,
    'November': 150.000,
    'December': 500.000
}

quarter_of_salles = {'QUARTER_OF_SALLES1': [month_of_salles['January'] + month_of_salles['February'] + month_of_salles['March'] / len(['QUARTER_OF_SALLES1'])],
                      'QUARTER_OF_SALLES2': [month_of_salles['April'] + month_of_salles['May'] + month_of_salles['June'] / len(['QUARTER_OF_SALLES2'])],
                      'QUARTER_OF_SALLES3': [month_of_salles['July'] + month_of_salles['August'] + month_of_salles['September'] / len(['QUARTER_OF_SALLES3'])],
                      'QUARTER_OF_SALLES4': [month_of_salles['October'] + month_of_salles['November'] + month_of_salles['December']/len(['QUARTER_OF_SALLES4'])]}
#Calculando a média:
#Utilizei o sum, pois ele tem a função de somar todas as vendas e o len lê uma venda de cada vez no dicionário.
average_sales = {quarter: sum(sales) / len(sales) for quarter, sales in quarter_of_salles.items()}
#Encontrando o maior valor e pegando a chave desse maior valor com o  key= e o .get
max_value_salles = max(quarter_of_salles, key=quarter_of_salles.get)
#Encontrando o menor valor e pgando a chave desse menor valor com o key= e o .get 
min_value_salles = min(quarter_of_salles, key=quarter_of_salles.get)

#Encontrando o valor de todas as vendas
total_sales = sum(month_of_salles.values())

print("The max value of quarter:", max_value_salles)
print("The min value of quarter:", min_value_salles)
print("The total average of year:", total_sales)

#Você tem um conjunto de dados que contém informações
#sobre a produção anual de diferentes culturas em diversas fazendas ao longo de vários anos. O objetivo é realizar
#uma análise simples desses dados usando apenas as funções agregadoras. Tarefas: Encontre o ano em que a
#produção total foi máxima e o ano em que foi mínima. Identifique a cultura que teve a maior produção total e a
#cultura com a menor produção total ao longo dos anos. Encontre a fazenda que obteve a produção máxima em um
#determinado ano e a fazenda com a produção mínima no mesmo ano.
#- Construa seus próprios dados fictícios.

#Criando o dicionário com os dados fictícios:
farm_production = {
    2000:{'soybeans': 20.000, 'corn': 30.000, 'fruits': 40.000},
    2001:{'soybeans':40.000, 'corn':60.000, 'fruits':80.000},
    2002:{'soybeans':60.000, 'corn':80.000, 'fruits':100.000},
    2003:{'soybeans':80.000, 'corn':100.000, 'fruits':150.00},
    2004:{'soybeans':120.000, 'corn':300.000, 'fruits':250.000},
    2005:{'soybeans':200.000, 'corn':450.000, 'fruits':999.999},

}
#ACHANDO O ANO COM A MAIOR E MENOR PRODUÇÃO:
#Criando uma variável que irá pegar o valor máximo do dicionário e junto a isso pegara a chave e a soma dos valores do mesmo
max_year_production = max(farm_production, key= lambda year: sum(farm_production[year].values()))
#Criando uma variável que irá pegar o valor mínimo do dicionário e junto a isso pegara a chave e asoma dos valores do mesmo.
min_year_production = min(farm_production, key= lambda year: sum(farm_production[year].values()))

#ACHANDO A MAIOR E MENOR CULTURA
#Utilizei o max para pegar o valor máximo dentro do dicionário, pegando a variável acima que criei utilizando a chave dela dentro do dicionário e pegando o get para extrair o valor
max_culture = max(farm_production[max_year_production], key=farm_production[max_year_production].get) 
#Utilizei da mesma lógica para pegar o valor mínimo
min_culture = min(farm_production[min_year_production], key=farm_production[min_year_production].get)

max_farm_in_max_year = max(farm_production[max_year_production], key=farm_production[max_year_production].get)
min_farm_in_min_year = min(farm_production[min_year_production], key=farm_production[min_year_production].get)

#Exibindo os dados:
print("The year with max total production is:", max_year_production)
print("The year with min total production is:", min_year_production)
print("The culture with max total production is:", max_culture)
print("The culture with min total production is:", min_culture)
print("The farm with max production in the max year is:", max_farm_in_max_year)
print("The farm with min production in the min year is:", min_farm_in_min_year)