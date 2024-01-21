#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

list1=[1,2,3,4,5,6,7,8,9,10]
list2=[11,12,13,14,15,16,17,18,19,20]

list3=[]

for i in range(len(list1)):
    list3.append(list1[i])
    list3.append(list2[i])

print(list3)