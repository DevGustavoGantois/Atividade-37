#Escreva um programa que percorra as chaves e valores
#de um dicionário separadamente e os exiba.

#Dicionário com as informações das pessoas
information_people = {
    'Name1': 'Gustavo',
    'Age1': '20',
    'City1': 'Salvador',
    'State1': 'BA',
    'Country1': 'Brazil',
    'Name2': 'Jose',
    'Age2': '21',
    'City2': 'Fortaleza',
    'State2': 'Ceará',
    'Country2': 'Brazil',
    'Name3': 'Vitor',
    'Age3': '22',
    'City3': 'Garulhos',
    'State3': 'São Paulo',
    'Country3': 'Brazil',

}

print("Keys")

# Percorre as chaves do dicionário:
for key in information_people.keys():
    print(key)
# Percorre os valores das pessoas do dicionário:
for value in information_people.values():
    print(value)