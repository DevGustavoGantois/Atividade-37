#Escreva uma função que recebe uma lista x e retorna x concatenada com ela mesma.

#Criando a função da lista
def concat_list(list):
    print("My List:", list)
    concat_list = list + list
    return concat_list

#Criando as listas:
list2=[1,2,3,4,5,6,7,8,9,10]
result_list = concat_list(list2)
#Imprimindo a a lista:
print("Concatened List:", result_list)

