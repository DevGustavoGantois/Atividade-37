#Crie uma função chamada concatenar_strings que
#aceita um número variável de strings como argumentos
#posicionais (usando *args). A função deve concatenar
#todas as strings em uma única string e retorná-la.

def concat_strings(*args):
    result = ''.join(args) #O .join é usado para unir strings, concatena-lás.
    return result
    
strings_concatened = concat_strings('Hello', 'How', 'are', 'you', '?!')
print(strings_concatened)
