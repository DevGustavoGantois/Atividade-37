#Crie uma função que receba um horário e imprima "Bom dia!","Boa tarde!" ou "Boa noite!" conforme o horário.

def print_day(hours_day):
    if 0<= hours_day < 24:
        if hours_day <= 12:
            print('Good Morning.')
        elif hours_day < 17:
            print('Good Afternon.')
        else:
            print('Good Night.')
    else:
        print("Invalid Hour. Please, enter value to 0 and 24 hours.")

#Solicitando ao usuário para inserir o horário do dia:
hours_day = float(input('Enter the hour of day (0-24):'))

#Chamando a função:
print_day(hours_day)