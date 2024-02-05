#Crie uma calculadora com opções de soma, multiplicação, subtração, divisão e sair. (Ela deverá funcionar infinitamente, até que o usuário decida sair da calculadora.)
#Utilize funções de rotina para cada operação e funções de unidade
#lógica para realizar os cálculos.
#Dica:
#Utilize de condicionais e Laços de Repetição para realizar esse
#exercício.

def numbers_sum(num1, num2):
    return num1 + num2
    #Essa função tem a funcionalidade de fazer uma adição entre num1 e num 2

def numbers_subtract(num1, num2):
     return num1 - num2
    #Essa função tem a funcionalidade de fazer uma subtração entre num 1 e num2 
def numbers_multiplication(num1, num2):
    return num1 * num2
    #Essa função tem a funcionalidade de fazer uma multiplicação entre num 1 e num 2
def numbers_division(num1, num2):
    #Essa função tem a funcionalidade de fazer uma divisão entre num 1 e num 2
    if num2 != 0:
        return num1/num2
    else:
        print('Error: division by zero.')


while True:
    print('<----------------------------------------------------->')
    print("Sum --> '1'")
    print("Subtract --> '2'")
    print("'Multiplication --> '3'")
    print("Division --> '4'")
    print("Exit Program --> '5'")
    print('<----------------------------------------------------------->')
    choose_operations = input('Choose Operation (1-5):')

    if choose_operations == '5':
        print("Thank You User! Finished Program.")
        break

    try:
        num1 = float(input("Enter a number 1:"))
        num2 = float(input("Enter a number 2:"))
    except ValueError:
        print('Invalid input. Please enter valid numbers.')
        continue
    else:
        if choose_operations == '1':
            result = numbers_sum(num1, num2)
            print(f"The sum between number 1 and number 2 -> {num1}+{num2} = {result}")
        elif choose_operations == '2':
            result = numbers_subtract(num1, num2)
            print(f'The subtract between number 1 and number 2 -> {num1}-{num2} = {result}')
        elif choose_operations == '3':
            result = numbers_multiplication(num1,num2)
            print(f"The multiplication between number 1 and number 2 -> {num1}x{num2} = {result}")           
        elif choose_operations == '4':
            result = numbers_division(num1,num2)
            print(f"The division between number 1 and number2 -> {num1}/{num2} = {result}")
        elif choose_operations == '5':
            print('Invalid choice. Please enter a number between 1 and 5.')

