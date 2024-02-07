#Crie uma função que aceita uma lista de strings e use a
#função reduce (importada de functools) para encontrar
#a maior string na lista.

from functools import reduce

def max_string_list(list_strings):
    if not list_strings:
        return None
    
    max_string = reduce(lambda x,y: x if len(x) > len(y) else y, list_strings)
    return max_string

list_of_strings = ["Apple", "Banana", "Orange", "Kiwi", "Strawberry"]
max_result_string = max_string_list(list_of_strings)

print('List of strings:', list_of_strings)
print('Bigger strings:', max_result_string)

