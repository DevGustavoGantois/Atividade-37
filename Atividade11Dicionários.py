#Desenvolva um programa que recebe um dicionário, uma
#chave e um valor como entrada e adiciona a chave e o
#valor ao dicionário, atualizando o valor se a chave já
#existir.
def receive_dictionary(key, value, dictionary):
    #Verifica se a chave já existe no dicionário
    if key in dictionary:
        print(f"The key in dictionary {key} exists. Updating the {value}")
    else:
        dictionary[key] = value
#Dicionário criado
my_dictionary = {'Gustavo': 20, 'Matheus': 22, 'Leandro': 25}
#Recebe entrada do usuário para chave e valor
key_user = input('Enter the key:')
value_user = input('Enter the value:')

#Coverte o valor para um tipo adequado(por exemplo, int)
try:
    value_user = int(value_user)
except ValueError:
    print("Error: Value must be an integer")
    exit()

#Chamando a função para adicionar ou atualizar a entrada no dicionário    
receive_dictionary(my_dictionary, key_user, value_user)

#Exibe o dicinário atualizado
print('Update Dictionary:', my_dictionary)