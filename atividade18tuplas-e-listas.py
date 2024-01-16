#Faça um programa que leia 4 notas de um aluno e imprima sua média. Após a média ser calculada,
#informe se o aluno foi ou não aprovado.
#a. Aprovado --- média maior ou igual a 7
#b. Reprovado --- média menor que 5
#c. Em recuperação --- média entre 5 e 7
addiction_of_notes=0

for i in range(1,5):
    notes=float(input(f"Enter a note {i} ->"))
    addiction_of_notes+=notes

result=addiction_of_notes/4


if result>=7:
    print("Aproved.")
elif result<5:
    print("Reproved.")
elif result>=5 or result<7:
    print("In recovery.")


print(f"The result of average is = {result:.2f}")

print("<------------------------------------------------------------------------------>")

notas=[float(input(f"Digite a nota {i + 1}:")for i in range(4))]

media=sum(notas)/len(notas)

print(f" A Média do aluno é de -> {media:.2f}")

if media>=7:
    print("Aprovado.")
elif media<5:
    print("Reprovado.")
elif media>=5 or media<7:
    print("Em Recuperação.")

#EXPLICAÇÃO DO CÓDIGO:
    
#1. A primeira forma eu fiz adicionando uma variável flag -> addiction_of_note = 0
#2. Usei um loop de repetição for para caso contar do número 1 a 5. (No problema está pedindo 4 notas de um aluno)
#3. Criei uma variável notes para armazenar os valores das notas desse aluno
#4. fiz com que a varável addiction_of_notes fose igual a soma das notas
#5.Criei uma variável result e dividi pelo valor número de notas pedidas(4)
#6.Usei estruturas condicionais, se o resultado fosse maior ou igual a 7, mostraria no terminal se o aluno foi aprovado ou reprovado, e assim por diante.
#<--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->
#1.Criei uma variável notar para armazenar os valores das 4 notas dentro de uma lista. Dentro da lista botei um input aliado a um for + 1 para somar do 1 em diante, não começar do zero.
#2.Criei uma variável média para armazenar a soma das notas dentro da lista com a função sum, e usei um len para ler cada elemtno dentro da variável notas. 
#3.Usei um print para mostrar o valor da média desse aluno.
#4. Usei um if para se média fosse maior ou igual a 7 aprovado elif...e assim por diante. 