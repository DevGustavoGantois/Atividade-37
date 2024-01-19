#Crie uma lista com 5 valores inteiros variados. E crie uma função que irá receber essa lista e imprimir a soma de todos os valores da lista.

# Criando a função
def print_list_and_sum(lst):
    print("List:", lst)
    sum_result = sum(lst)
    print("Sum of all values in the list:", sum_result)

# Criando a lista
list_values = [25, 44, 12, 34, 45]

# Chamando a função para imprimir a lista e a soma dos valores
print_list_and_sum(list_values)



