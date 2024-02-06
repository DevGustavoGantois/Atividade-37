#1.Crie uma função que receba um nome e imprima uma saudação personalizada.

def print_name(name):
    #Essa função retorna uma saudação ao nome do usuário.
    print(f'Hello {name}!')

name = input('Enter your name:')

print_name(name)

#2.Crie uma função que receba um horário e imprima "Bom dia!","Boa tarde!"ou"Boa noite!" conforme o horário.

def print_hours_day(hour):
    if hour <= 12:
        print('Hello! Good morning.')
    elif hour < 17:
        print('Hello! Good afternoon.')
    elif hour >= 18:
        print('Hello! Good Night.')
    else:
        print('This hour not exist.')

hour = float(input('Enter what time it is(0-24):'))

result_hour = print_hours_day(hour)
print(result_hour)

#3.Crie uma função que receba dois números e retorne a soma deles.
def print_sum(num1, num2):
    return num1 + num2

num1 = float(input('Enter a number 1:'))
num2 = float(input('Enter a number 2:'))
    

result_sum = print_sum(num1, num2)
print(f"{num1}+{num2}=",result_sum)

#4.Crie uma função que receba dois números e retorne a subtração do primeiro pelo segundo.

def print_subtract(number1, number2):
    return number1 - number2

number1 = float(input("Enter a number 1:"))
number2 = float(input("Enter a number 2:"))

result_subract = print_subtract(number1, number2)

print(f"{number1} - {number2} =", result_subract)

#5.Crie uma função que receba dois números e retorne a multiplicação deles.

def print_multiplication(n1, n2):
    return n1 * n2

n1 = float(input("Enter a number 1:"))
n2 = float(input("Enter a number 2:"))

result_multiplication = print_multiplication(n1,n2)

print(f"The multiplication of {n1}x{n2}=", result_multiplication)

#6.Crie uma calculadora com opções de soma, multiplicação, subtração, divisão e sair.(Ela deverá funcionar infinitamente, até que o usuário decida sair da
#calculadora.)Utilize funções de rotina para cada operação e funções de unidade lógica para realizar os cálculos. 
#Dica:Utilize de condicionais e Laços de Repetição para realizar esse exercício.

def operation_sum(num1, num2):
    return num1 + num2

def operation_subtract(num1, num2):
    return num1 - num2

def operation_multiplication(num1, num2):
    return num1 * num2

def operation_division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        print('Error: Division by zero.')
        return None  # Adicionei um retorno para evitar problemas em caso de divisão por zero.

while True:
    print('<------------CALCULATION OPERATIONS ------------------->')
    print('<----------------------------------------->')
    print("Choose number for Sum --> '1'")
    print("Choose number for Subtract --> '2'")
    print("Choose number for Multiplication --> '3'")
    print("Choose number for Division --> '4'")
    print("Choose number for Exit the Program for --> '5' ")
    print('<-------------------------------------------------->')

    Choose_operations = input("Choose the number 1-5 (Type '5' to exit the program):")

    if Choose_operations == '5' or Choose_operations.lower() == 'exit the program':
        print('Thank You User!! Finish the program...')
        break

    try:
        num1 = float(input("Enter a number 1:"))
        num2 = float(input("Enter a number 2:"))
    except ValueError:
        print('Invalid number. Enter a valid number...')
        continue

    if Choose_operations == '1':
        result_sum = operation_sum(num1, num2)
        print(f'The result of sum -> {num1} + {num2} = {result_sum}')
    elif Choose_operations == '2':
        result_subtract = operation_subtract(num1, num2)
        print(f'The result of subtract -> {num1} - {num2} = {result_subtract}')
    elif Choose_operations == '3':
        result_multiplication = operation_multiplication(num1, num2)
        print(f'The result of multiplication -> {num1} x {num2} = {result_multiplication}')
    elif Choose_operations == '4':
        result_division = operation_division(num1, num2)
        if result_division is not None:
            print(f'The result of division -> {num1} / {num2} = {result_division}')

