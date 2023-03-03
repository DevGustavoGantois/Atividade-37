print('==========================================ATIVIDADE===================================================')
print("""Faça um programa que leia 5 valores númericos e guarde-os em uma lista. No final, mostre qual foi
 o maior e o menor valor digitado e suas respectivas posições na lista. 
 ==============================================================================================================""")
listanum = []
bigger = 0
smaller = 0
for v in range(0, 5):
    listanum.append(input('Type one number {} for the position:'.format(v)))
    if v == 0:
        bigger = smaller = listanum[v]
    else:
        if listanum[v] > bigger:
            bigger = listanum[v]
        if listanum[v] < smaller:
            smaller = listanum[v]
print('=-'* 30)
print(f'The bigger valor is: {listanum}.')
print(f'The smell valor is: {bigger}.')
print(f'The positions in list is: {smaller}')