#Faça um Programa que leia 4 notas, mostre as notas e a média na tela. (Use lista para armazenar as notas)


#Criei uma lista com os 4 valores das notas.
note_list=[2.5, 8.2, 4.7, 10]
#Calculei a média usando a função sum para calcular os valores dentro da lista e dividir ela pela quantidade de notas.
average = sum(note_list) / 4
#Usei estrutura condicional, se média > 6 Aprovado, se não Reprovado, e assim por diante...
if average > 6:
    print("Aproved.")
elif average < 5:
    print("Reproved")
else:
    print("Error. The value is not exist...")
#Mostrei o valor da média na tela através do print. 
print(f"Average of student is = {average}")

