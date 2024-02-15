#Crie um módulo chamado manipulacao_strings que
#contenha funções para realizar operações com strings,
#como inverter uma string, contar o número de palavras
#em uma string e verificar se uma string é um
#palíndromo (lê-se igual de trás para frente). Crie
#um programa principal que importe o módulo e use
#essas funções com strings fornecidas pelo usuário.

def reverse_string(string):
    #Inverte a string 
    return string[::-1]

def count_string(string):
    #Conta o número de palavras da sitrng
    return len(string.split())

def palindrome_string(string):
    #Se a string for igual a string ela vai inverter a string, se n retornar false.
    return string == string[::-1]
    