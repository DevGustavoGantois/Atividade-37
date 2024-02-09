#Considere uma lista de números inteiros 
#umeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Utilizando as funções map(),filter() e reduce(), escreva um código que execute as seguintes operações:
#Função map() para obter uma nova lista com o quadrado de cada número da lista numeros
#Função filter() para obter uma nova lista com números pares da lista numeros
#Função reduce()  para obter a soma de todos os números da lista numeros
#Qual o resultado obtido após a execução das operações acima?

lista_numeros_inteiros = [1,2,3,4,5,6,7,8,9,10]

from functools import reduce

nova_lista = list(map(lambda x: x ** 2, lista_numeros_inteiros))

nova_lista_numeros_pares = list(filter(lambda x: x % 2 == 0, lista_numeros_inteiros ))

soma_lista_numeros = reduce(lambda x, y: x + y, lista_numeros_inteiros)

print("Nova lista com o quadrado de todos os números presentes da lista original ->",nova_lista)
print("Nova lista com os números pares da original ->",nova_lista_numeros_pares)
print("Soma de todos os números da lista ->",soma_lista_numeros)
