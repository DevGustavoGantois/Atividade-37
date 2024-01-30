#Crie um programa que receba uma lista de números e remova todas as duplicatas usando um conjunto (set). Em seguida, exiba a lista original e a lista sem duplicatas.

def remove_duplicates (list):
    #Converte a lista para um conjunto para remover duplicatas 
    set_not_duplicates = set(list)
    #Coverte o conjunto de volta para uma lista
    list_not_duplicates = list(set_not_duplicates)

    return list_not_duplicates

#Recebe uma lista de números do usuário 
numbers = input('Enter a space separated list of numbers:').split()

#Converte os números para inteiros 
numbers = [int(num) for num in numbers]

#Exibe a lista original 
print('Original list:', numbers)

#Remove as duplicatas usando a função definida anteriormente
numbers_not_duplicates = remove_duplicates(numbers)

#Exibe a lista sem duplicatas
print('List without duplicates:', numbers_not_duplicates)