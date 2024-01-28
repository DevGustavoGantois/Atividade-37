#Crie um programa que recebe dois conjuntos e exibe a interseção deles.

#Função para receber conjuntos do usuário
def receive_set():
    elements = input("Enter a elements of separate for spaces:")
    list_elements=elements.split()
    set = set(list_elements)
    return set

#Recebe dois conjuntos do usuário
print("Enter a set of elements of first set:")
set1 = receive_set()

print("\nEnter a elements of second set:")
set2 = receive_set()

#Calcula e exibe a interseção dos conjuntos:
intersection = set1.intersection(set2)
print('\nThe intersection of sets is:', intersection)
