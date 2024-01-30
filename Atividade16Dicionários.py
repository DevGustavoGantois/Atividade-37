#Crie um programa que realize a união de múltiplos conjuntos e exiba o conjunto resultante.

def union_sets(*sets):
    #Usa o operador | (pipe) para realizar a união de conjuntos
    result_sets = set().union(* sets)
    return result_sets

sets1 = {11,22,33}
sets2 = {44,55,66}
sets3 = {77,88,99}

#Realiza a união de conjuntos
result_sets  = union_sets(sets1, sets2, sets3)

#Exibe o conjunto resultante
print('Result union of sets:', result_sets)