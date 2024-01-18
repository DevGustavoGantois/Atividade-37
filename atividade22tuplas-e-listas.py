#Faça um programa que leia o nome de 4 vendedores e o valor total de venda que cada um realizou.
#Imprima na tela os 2 vendedores que mais venderam, ordem decrescente.

total_sales = []

for i in range(4):
    name = input(f"Enter your name user {i + 1} -> ")
    sale = float(input(f"Enter your sale {name}: "))
    
    total_sales.append({'name': name, 'sale': sale})

# Ordena a lista total_sales em ordem decrescente com base no valor da venda
descending_value = sorted(total_sales, key=lambda x: x['sale'], reverse=True)

print("The two sellers who sold the most in descending order:")
for seller in descending_value[:2]:
    print(f"Name: {seller['name']}, Sale: {seller['sale']}")

#EXPLICAÇÃO DO CÓDIGO:
#1.Criei um array chamado vendas totais-> total_sales.
#2.Usei um laço de repetição for para ler todos os 4 nomes pedidos no enunciado e as 4 vendas de cada nome também. Criei variáveis name e sale para 
#3.Utilizei um append dentro do array total_sales, mostrando o nome e a venda dentro do array
#4.Criei uma variável chamada ordem decrescente, essa varável irá botar a lista em ordem e usei uma key=lambdapara ordenar a lista com base no valor da chave de cada dicinário, uma função de ordenacção, 
#5.Usei o reversed=True para a ordenação ser em ordem decrescente.
#6.Utilizei um print para mostrar os 2 maiores vendedores em ordem decrescente
#7.Utilizei um for com mostrando somente os 2 maiores valores em ordem decrescente por iss[:2]
#8.e usei um print para mostrar o valor decrescente da venda junto aos nomes dos vendedores.

    

