#Crie uma função que receberá duas listas de valores inteiros e irá imprimir a soma do item do primeiro índice da primeira lista, com o último item da segunda lista.
def print_sum_of_lists(list1, list2):
#Verfica se as listas não estão vazias
    if not list1 or not list2:
        print("At least one of the lists is empty. Unable to calculate the sum.")
        return 
    
    #Calcula a soma do item do primeiro índice da primeira lista com o último:
    sum_result = list1[0] + list2[-1]

    #Imprime as listas e a soma calculada
    print("List 1:", list1)
    print("List 2:", list2)
    print(f"The sum of first item of List 1 with the last item of List 2: {sum_result}.")

    #Minhas 2 Listas:
list_one = [31, 29, 8, 7, 9, 5, 4, 55, 58]
list_two = [66, 82, 34, 22, 15, 20, 30, 99]

#Chamar função para imprimir as listas e a soma calculada
print_sum_of_lists(list_one, list_two)