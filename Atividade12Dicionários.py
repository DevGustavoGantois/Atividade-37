#Escreva um programa que recebe um dicionário e uma
#lista de chaves como entrada e verifica se todas as
#chaves da lista existem no dicionário. A função deve
#retornar True se todas as chaves existirem e False caso
#contrário.


def receive_items(dictionary, list_keys):
    for key in list_keys: 
        if key not in dictionary: 
            return False
    return True


my_dictionary = {'Ovos', 8.00, 'Abacaxi', 6.00, 'Frango kg', 20.00}
list_verification_keys = ['Ovos', 'Abacaxi', 'Frango kg']


result = receive_items(my_dictionary, list_verification_keys)
print("All keys exists in dictionary", result)


#EXPLICANDO O CÓDIGO:
#Criando a função para verificar as chaves da lista que existem no dicionário
#for foi usado para percorrer as chaves do dicionário.
#Se as chaves não estiverem no dicionário, retorna falso, se estiverem, retorna verdadeiro
#Criando o dicionário
#Criando a lista com as chaves do dicionário dentro.
#criando a variável resultado para armazenar a função junto com as variáveis 
#Mostrando o resultado no terminal com o print.