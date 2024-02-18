#Crie um dicionário com informações de produtos,
#incluindo nome, preço e quantidade em estoque.
#Implemente funções para adicionar, remover e atualizar
#produtos no dicionário.

dict_product_information = {}

def add_products():
    name = input("Enter a name of product:")
    price = input("Enter a price of product:")
    quantity = input("Enter a quantity of product:")
    product_information = {'name': name, 'price': price, 'quantity': quantity}
    dict_product_information[name] = product_information
def remove_products():
    name = input("Do you want to remove a product from the list:")
    if name in dict_product_information:
        del dict_product_information[name]
        print(f"{name} has benn removed from the product list.")
    elif name.lower() == 'no':
        print(f"The product {name} is not in the list...")
    else:
        print("The word is not exist.")

def update_product():
    name = input("Do you want to quantity update a product:")
    if name in dict_product_information:
        quantity = int(input("Enter the new quantity:"))
        dict_product_information[name]['quantity'] = quantity
        print(f"Quantity for {name} has been updated to {quantity}.")
    else:
        print(f"The product {name} is not in the list.")

def main():
    while True:
        print("PRODUCT LIST")
        print("<==========================>")
        print("1->Add Product")
        print("2->Remove Product")
        print("3->Update Product")
        print("4->Exit the program")
        print("<============================>")

        option = input("Enter a options in product list:")

        if option == '1':
            add_products()
        elif option == '2':
            remove_products()
        elif option == '3':
            update_product()
        elif option == '4':
            print("The program is finished...")
            break
        else:
            print("The option is invalid, type to (1-4).")

if __name__ == '__main__':
    main()

