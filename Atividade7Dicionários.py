#Escreva um programa que receba duas listas e calcule a união
#dos elementos únicos dessas listas, usando conjuntos.

def calculate_union(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    uniao = set1.union(set2)

    return uniao

list1 = ['Melo', 'Murilo', 'Gustavo', 'Matheus', 'Jorge', 'Rodrigo', 'Cauã']
list2 = ['Melo', 'Gustavo', 'Matheus', 'Pedro', 'Pablo', 'Luan', 'Jose', 'Moyses']

resultado_uniao = calculate_union(list1, list2)
print("The union of the single elements of the list is:", list(resultado_uniao))
