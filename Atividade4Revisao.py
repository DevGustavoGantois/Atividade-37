#Crie uma função que receba uma lista de strings e
#retorne uma nova lista contendo apenas as strings
#palíndromos.

palindromes_list=['aia', 'ama', 'ata', 'esse', 'Gustavo', 'Augusto', 'Nayra']

def list_strings(input_list):

    result = [word for word in input_list if word.lower() == word.lower()[::-1]]
    return result
    
result_palindromes_list = list_strings(palindromes_list)
print(result_palindromes_list)
    