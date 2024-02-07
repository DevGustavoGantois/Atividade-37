#Crie uma função que aceite dois números e uma
#operação (por exemplo, adição, subtração,
#multiplicação, divisão) como argumentos e use funções
#lambda para realizar a operação especificada. A função
#deve retornar o resultado da operação.

def operation_numbers(number1, number2, operation):
    if operation == 'addition':
        result = lambda x: number1 + number2
    elif operation == 'subtract':
        result = lambda x: number1 - number2
    elif operation == 'multiply':
        result = lambda x: number1 * number2
    elif operation == 'divide':
        result = lambda x: number1 / number2
    else:
        return 'Invalid operation.'
    
    return result(operation)

number1 = float(input('Enter a number 1:'))
number2 = float(input('Enter a number 2:'))
operation = input('Enter the Operation (addition, subtract, multiply, divide):')

result = operation_numbers( number1, number2, operation)
print('Result:',result)