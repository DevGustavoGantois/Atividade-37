#1.Crie um programa que solicita ao usuário que insira três
#notas e, em seguida, calcule a média dessas notas
#usando uma função. A função deve receber as três
#notas como argumentos e retornar a média. Por fim, o
#programa deve imprimir a média calculada.

def calculate_average(note1, note2, note3):
    average = (note1 + note2 + note3) / 3
    return average

note1 = float(input("Enter a note 1:"))
note2 = float(input("Enter a note 2:"))
note3 = float(input("Enter a note 3:"))

result = calculate_average(note1, note2, note3)
print(f'The result average of note1 -> ({note1} + {note2} + {note3}) / 3 --> {result:.2f}')

#2.Crie um programa que define uma função calcular_area_retangulo que recebe dois argumentos,
#comprimento e largura de um retângulo, e retorna a área desse retângulo. Em seguida, o programa deve
#solicitar ao usuário que insira o comprimento e a largura e imprimir a área calculada.

def calculate_area_of_rectangle(height, width):

    area = width * height
    return area

width = float(input("Enter the width of the rectangle:"))
height = float(input("Enter the height of the rectangle:"))

result = calculate_area_of_rectangle(height, width)
print(f"The Area of rectangle is -> {result:.2f}")

#3.Crie uma função chamada concatenar_strings que aceita um número variável de strings como argumentos
#posicionais (usando *args). A função deve concatenar
#todas as strings em uma única string e retorná-la.

def concat_strings(*args):
    result = "".join(args)
    return result


string_text= ['Gustavo','do you like', 'coffe?']

result = concat_strings(*string_text)
print(f"The string -> {result}")

#4.Crie uma função que aceita uma lista de números e use
#a função map para retornar uma nova lista contendo o
#dobro de cada número na lista de entrada.

def list_numbers(list_double):
    doubled_list = list(map(lambda x: x * 2, list_double))
    return doubled_list


numbers_of_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

result_list = list_numbers(numbers_of_list)
print(result)

#5.Crie uma função que aceita uma lista de números e use a função filter para retornar uma nova lista contendo apenas os números pares da lista de entrada.

def list_numbers_pair(numbers_pair):
    pair_list_numbers = list(filter(lambda x: x % 2 == 0, numbers_pair))
    return pair_list_numbers

numbers_pair = [1,2,3,4,5,6,7,8,9,10]

result = list_numbers_pair(numbers_pair)
print(result)

#6.Crie uma função que aceita uma lista de strings e use a
#função reduce (importada de functools) para encontrara maior string na lista.

import functools 

def list_strings(bigger_string_of_list):
    if not bigger_string_of_list:
        return None
    #Aqui usamos a função anonima lambda para comparar se uma string e maior que a outra no bigger_string_of_list:
    bigger_string = functools.reduce(lambda x, y: x if len(x) > len(y) else y, bigger_string_of_list)
    return bigger_string

bigger_list_of_string = ['Python', 'Java', 'C++', 'JavaScript', 'Ruby']

result = list_strings(bigger_list_of_string)
print(f"The bigger string is: {result}")

#7.Crie uma função chamada criar_lista_de_compras que 
#aceita um número variável de itens de compras como 
#argumentos posicionais (usando *args). A função deve
#criar e retornar uma lista de compras que contenha todos os itens fornecidos.

def create_list(*args):
    return list(args)

result = create_list('Apple', 'Orange', 'Cherry', 'Strawberry', 'grapes', 'Banana')
print(f'Result --> {result}')

#8.Crie uma função que aceite dois números e uma operação (por exemplo, adição, subtração,
#multiplicação, divisão) como argumentos e use funções lambda para realizar a operação especificada. A função
#deve retornar o resultado da operação.

def calculate_operations(number1,number2,operation):
    if operation.lower() == 'add':
        result = number1 + number2
        return result
    elif operation.lower() == 'subtract':
        result = number1 - number2
        return result
    elif operation.lower() == 'mmultiplication':
        result = number1 * number2
        return result
    elif operation.lower() == 'division':
        result = number1 / number2
        return result

print("VIRTUAL CALCULATOR")
print("<---------------------------------------------------->")
print("Add -> +")
print("subtract -> -")
print("Multplication -> * ")
print("Division -> /")
print("<--------------------------------------------->")
operation = input("Enter the operation into the calculator:")
number1 = float(input("Enter a number 1:"))
number2 = float(input("Enter a number 2:"))

result_operations = calculate_operations(number1, number2, operation)
print(f"The result of operation -> {result_operations}")

#Crie um processador de texto simples que realiza várias operações
#em um texto de entrada, como contar palavras, contar letras,
#inverter o texto e substituir palavras-chave. Requisitos:
#Crie uma função chamada processador_texto que aceite uma string de texto como argumento.
#A função deve aceitar uma série de operações como argumentos
#de palavra-chave, usando **kwargs. As operações podem incluir
#"contar_palavras","contar_letras","inverter_texto"e
#"substituir_palavra".Use funções lambda para realizar as operações de acordo com
#as palavras-chave especificadas nos argumentos de palavra-chave.
#Se a operação "substituir_palavra " for especificada, a função
#deve aceitar uma palavra-chave adicional, como "substituir_palavra"e"nova_palavra", para realizar a
#substituição em todo o texto. A função deve retornar o texto resultante após todas as operações.

def text_processor(text, **kwargs):
    # Operation to count words
    count_words = kwargs.get('count_words', False)
    if count_words:
        text = lambda t: f"Total words: {len(t.split())}"

    # Operation to count letters
    count_letters = kwargs.get('count_letters', False)
    if count_letters:
        text = lambda t: f"Total letters: {len([c for c in t if c.isalpha()])}"

    # Operation to reverse the text
    reverse_text = kwargs.get('reverse_text', False)
    if reverse_text:
        text = lambda t: t[::-1]

    # Operation to replace a word
    replace_word = kwargs.get('replace_word', False)
    new_word = kwargs.get('new_word', '')
    if replace_word and new_word:
        text = lambda t: t.replace(replace_word, new_word)

    # Apply the operations on the text
    result = text(text)
    
    return result

# Example usage
input_text = "This is an example text."

processed_result = text_processor(input_text, count_words=True, count_letters=True, reverse_text=True, replace_word='example', new_word='modified_example')

print(processed_result)

#Considere uma lista de números inteiros 
#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Utilizando as funções map(),filter() e reduce(), escreva um código que execute as seguintes operações:
#Função map() para obter uma nova lista com o quadrado de cada número da lista numeros
#Função filter() para obter uma nova lista com números pares da lista numeros
#Função reduce()  para obter a soma de todos os números da lista numeros
#Qual o resultado obtido após a execução das operações acima?

int_numbers_list = [1,2,3,4,5,6,7,8,9,10]

from functools import reduce

square_of_each_number = list(map(lambda x: x ** 2, int_numbers_list))
new_list_pair = list(filter(lambda x: x % 2 == 0, int_numbers_list))
sum_of_numbers_list = reduce(lambda x,y: x+y, int_numbers_list)

print(f"The original list -> {int_numbers_list}")
print(f"The list with square of each number ->{square_of_each_number}")
print(f"The list pair numbers -> {new_list_pair}")
print(f"The sum numbers of list -> {sum_of_numbers_list}")
