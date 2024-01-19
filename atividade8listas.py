#Crie uma lista com 5 valores inteiros e escreva uma função que receberá essa lista que irá retornar a soma dos três últimos itens da lista.

#Criando a função
def sum_last_three(lst):
    sum_list = sum(lst[-3:])
    return sum_list

#Criando a lista:
lst = [14,56,77,44,99]
#Pegando a variável sum_list e retornando a função sum_last_three(lst)
sum_list = sum_last_three(lst)
#Exibindo o valor da soma dos 3 últimos componentes da lista:
print("The result of sum of 3 last components of list is:", sum_list)