#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números ÍMPARES no vetor ímpar. Imprima os três vetores.

#Lista de 20 números:
list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,20]
#Lista para números pares e números ímpares
list_pair=[]
list_odd=[]
#Loop para verificar cada número e separá-los em list_pair e list_odd:
for num in list:
    if num % 2 == 0:
        list_pair.append(num)
    else:
        list_odd.append(num)
#Imprimindo as três listas
print('Lista Original:',list)
print('Números Pares:', list_pair)
print('Números ímpares:', list_odd)