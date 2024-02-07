#Crie uma função que aceita uma lista de números e use 
#a função map para retornar uma nova lista contendo o
#dobro de cada número na lista de entrada.

def numbers_list(input_list):
    #A expressão lambda é usada retornar o dobro do valor em forma de lista:
    doubled_numbers = list(map(lambda x: x * 2, input_list))
    return doubled_numbers

#Criando a lista
input_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
result = numbers_list(input_list)

#Lista normal:
print('Original list:', input_list)
#lista * 2:
print('Result of doubled numbers list :', result)