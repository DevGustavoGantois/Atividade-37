print('==========================================ATIVIDADE===================================================')
print("""Faça um programa que leia 5 valores númericos e guarde-os em uma lista. No final, mostre qual foi
 o maior e o menor valor digitado e suas respectivas posições na lista. 
 ==============================================================================================================""")
lc=[]

for x in range(0,5):
    conta = int (input(f"Digite um número {x}°: "))
    lc.append(conta)

 
print(f"maior valor {max (lc)}")
print(f"menor valor {min (lc)}")


for x in lc:
 print(f"posição: {lc} ")