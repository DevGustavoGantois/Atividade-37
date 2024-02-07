#Crie uma função que aceita uma lista de números e use a função filter para retornar uma nova lista contendo
#apenas os números pares da lista de entrada.

def list_numbers(input_list):
    pair_numbers = list(filter(lambda x: x % 2 == 0, input_list))
    return pair_numbers

input_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

result = list_numbers(input_list)
print('The pair is ->', result)