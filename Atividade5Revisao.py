#Dado um dicionário que representa as vendas de produtos, encontre o produto mais 
#vendido (ou os produtos mais vendidos, se houver um empate).

buy_products = {
    'computer': 30,
    'tv': 60,
    'bed': 70,
    'keyboard': 90
}

def more_salle_items(sales):
    max_sales = max(sales.values())
    best_selling_products = [product for product, quantity in sales.items() if quantity == max_sales]
    return best_selling_products

result_sales = more_salle_items(buy_products)
print("Top selling products:",result_sales)