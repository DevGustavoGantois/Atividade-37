#Crie uma função chamada criar_lista_de_compras que
#aceita um número variável de itens de compras como
#argumentos posicionais (usando *args). A função deve
#criar e retornar uma lista de compras que contenha
#todos os itens fornecidos.

def create_list_of_buy(*args):
        concat_items = list(args)
        return concat_items

items = input("Enter the items of list (separated by commas):")
items_list = items.split(',')

result = create_list_of_buy(*items_list)
print(result)
